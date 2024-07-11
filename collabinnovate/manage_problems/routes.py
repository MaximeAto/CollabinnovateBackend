

from datetime import datetime
import random
from faker import Faker
from flask import Blueprint, jsonify, request, abort
from sqlalchemy.exc import SQLAlchemyError

from collabinnovate import db
from collabinnovate.manage_problems.model import Problem
from collabinnovate.manage_user_accounts.account.model import Account
from collabinnovate.manage_user_accounts.user.model import User
from .mashmallow import MashmallowProblem
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
        about_problem=fake.paragraph(nb_sentences=5),
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
@problems.route("/add/<username>", methods=["POST"])
def create_problem(username):
    data = request.get_json()
    user = User.query.filter_by(email=username).first()
    account = Account.query.filter_by(user_id = user.id).first()
    required_fields = ['problemTitle', 'country', 'city', 'category', 'deadline',
                   'business_needs_improvement', 'population_affected', 
                   'concern_population_affected', 'impacts_on_these_populations',
                   'population_volume', 'problemTitle']

    
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    
    try:
        # Convertir la deadline en date (sans l'heure)
        deadline = datetime.strptime(data['deadline'], '%Y-%m-%d').date()
        
        new_problem = Problem(
            author = user.full_name,
            account_id=account.id,
            title=data['problemTitle'],
            about_problem = data['aboutProblem'],
            country=data['country'],
            city=data['city'],
            category=data['category'],
            deadline=deadline,
            activity_requiring_improvement=data.get('business_needs_improvement'),
            affected_population=data.get('population_affected'),
            concerns_of_affected_population=data.get('concern_population_affected'),
            impact_on_affected_population=data.get('impacts_on_these_populations'),
            quantitative_volume_affected_population=data.get('population_volume')
        )
        db.session.add(new_problem)
        db.session.commit()
        return jsonify({"message": "The problem has been added with success", "id": new_problem.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": "Registration error"}), 400
    except ValueError as e:
        return jsonify({"message": "Registration error"}), 500
    

@problems.route("/all", methods=["GET"])
def get_problems():
    try:
        problems_query = Problem.query.all()
        problems_list = [problem.to_dict() for problem in problems_query]
        return jsonify(problems_list), 200
    except SQLAlchemyError as e:
        # Log the error (optional)
        print(f"Database error: {e}")
        return jsonify({"error": "Database error occurred"}), 500
    except Exception as e:
        # Log the error (optional)
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


# Obtenir un problème spécifique par ID
@problems.route("/get/<int:id>", methods=["GET"])
def get_problem(id):
    try:
        problem = Problem.query.filter_by(id=id).first()
        if problem:
            return jsonify(problem.to_dict()), 200
        else:
            return jsonify({"error": "Problem not found"}), 404
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving the problem"}), 500

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



