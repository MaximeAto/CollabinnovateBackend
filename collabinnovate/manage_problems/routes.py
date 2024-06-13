
import random
from faker import Faker
from flask import Blueprint, jsonify, request, abort
from sqlalchemy.exc import SQLAlchemyError

from collabinnovate import db
from collabinnovate.manage_problems.model import Problem

problems = Blueprint('problems', __name__)
fake = Faker()

# Générer de faux problèmes
@problems.route("/fake_problems", methods=["POST"])
def thousand_problems():
    for _ in range(1000):
        generate_fake_problems()
    return jsonify(message="Les 1000 problèmes ont été enregistrés"), 201


def generate_fake_problems():

    accounts_id = list(range(1, 21))
    categories = ['Health', 'Education', 'Infrastructure', 'Environment', 'Safety']
    countries = ['USA', 'Canada', 'France', 'Germany', 'Australia']
    cities = ['New York', 'Toronto', 'Paris', 'Berlin', 'Sydney']

    problem = Problem(
        account_id=fake.random_element(elements=accounts_id),
        title=fake.sentence(nb_words=6),
        country=fake.random_element(elements=countries),
        city=fake.random_element(elements=cities),
        category=fake.random_element(elements=categories),
        deadline=fake.date_time_between(start_date='now', end_date='+30d'),
        activity_requiring_improvement=fake.text(max_nb_chars=200),
        affected_population=fake.paragraph(nb_sentences=3),
        concerns_of_affected_population=fake.paragraph(nb_sentences=3),
        impact_on_affected_population=fake.paragraph(nb_sentences=3),
        quantitative_volume_affected_population=random.randint(1, 2000)
    )
    db.session.add(problem)
    db.session.commit()

# Créer un nouveau problème
@problems.route("/add", methods=["POST"])
def create_problem():
  data = request.get_json()
  try:
      new_problem = Problem(
          account_id=data['account_id'],
          title=data['title'],
          activity_requiring_improvement=data.get('activity_requiring_improvement'),
          affected_population=data.get('affected_population'),
          concerns_of_affected_population=data.get('concerns_of_affected_population'),
          impact_on_affected_population=data.get('impact_on_affected_population'),
          quantitative_volume_affected_population=data.get('quantitative_volume_affected_population')
      )
      db.session.add(new_problem)
      db.session.commit()
      return jsonify(new_problem.id), 201
  except SQLAlchemyError as e:
      db.session.rollback()
      abort(400, description=str(e))

# Obtenir la liste de tous les problèmes
@problems.route("/all", methods=["GET"])
def get_problems():
  problems_list = Problem.query.all()
  return jsonify([problem.to_dict() for problem in problems_list])

# Obtenir un problème spécifique par ID
@problems.route("/get/<int:id>", methods=["GET"])
def get_problem(id):
  problem = Problem.query.get_or_404(id)
  return jsonify(problem.to_dict())

# Mettre à jour un problème existant
@problems.route("/update/<int:id>", methods=["PUT"])
def update_problem(id):
  data = request.get_json()
  problem = Problem.query.get_or_404(id)
  try:
      problem.account_id = data.get('account_id', problem.account_id)
      problem.title = data.get('title', problem.title)
      problem.activity_requiring_improvement = data.get('activity_requiring_improvement', problem.activity_requiring_improvement)
      problem.affected_population = data.get('affected_population', problem.affected_population)
      problem.concerns_of_affected_population = data.get('concerns_of_affected_population', problem.concerns_of_affected_population)
      problem.impact_on_affected_population = data.get('impact_on_affected_population', problem.impact_on_affected_population)
      problem.quantitative_volume_affected_population = data.get('quantitative_volume_affected_population', problem.quantitative_volume_affected_population)
      
      db.session.commit()
      return jsonify(problem.to_dict()), 200
  except SQLAlchemyError as e:
      db.session.rollback()
      abort(400, description=str(e))

# Supprimer un problème
@problems.route("/delete/<int:id>", methods=["DELETE"])
def delete_problem(id):
  problem = Problem.query.get_or_404(id)
  try:
      db.session.delete(problem)
      db.session.commit()
      return jsonify(message="Le problème a été supprimé avec succès"), 200
  except SQLAlchemyError as e:
      db.session.rollback()
      abort(400, description=str(e))



