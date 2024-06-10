import random
from flask import Blueprint, json, jsonify, request
from collabinnovate import db
from faker import Faker

from collabinnovate.manage_solutions.model import Solution


solutions = Blueprint('solutions', __name__)
fake = Faker()

def faker_solution ():
    accounts_id = list(range(1, 21))
    prolems = list(range(1,1001))

    solution = Solution(
    account_id = fake.random_element(elements=accounts_id),
    problem_id = fake.random_element(elements=prolems),
    title=fake.company(),
    description=fake.paragraph(),
    product_offered=fake.word(),
    service_offered=fake.word(),
    customer_expectations=fake.paragraph(),
    what_company_sells=fake.word(),
    how_product_service_marketed=fake.paragraph(),
    customer_access_method=fake.word(),
    competitors=json.dumps([fake.company() for _ in range(random.randint(1, 5))]),
    direct_sales=fake.boolean(),
    direct_sales_details=fake.paragraph(),
    wholesale=fake.boolean(),
    informal=fake.boolean(),
    advertising=fake.boolean(),
    direct_marketing=fake.boolean(),
    sales_promotion=fake.boolean(),
    display=fake.boolean(),
    word_of_mouth=fake.boolean(),
    trade_show=fake.boolean(),
    mail_order=fake.boolean(),
    human_resources=json.dumps([
        {
            "position": fake.job(),
            "tasks_to_perform": fake.sentence(),
            "required_skills_experience": fake.sentence(),
            "ideal_profile": fake.sentence(),
            "monthly_salary": fake.random_int(1000, 5000)
        }
    ]),
    legal_form=fake.word(),
    financing_needed=fake.word(),
    investment_characteristics=fake.paragraph(),
    suppliers=json.dumps([fake.company() for _ in range(random.randint(1, 5))]),
    amount=fake.random_int(1000, 10000),
    variable_cost=fake.random_int(100, 1000),
    fixed_cost=fake.random_int(100, 1000),
    offers=json.dumps([
        {
            "Offer_Name": fake.word(),
            "Offer_Price": fake.random_int(10, 100),
            "Quantity_Sold": fake.random_int(1, 10),
            "Revenue_Generated": fake.random_int(100, 1000),
            "For_One_Month": fake.random_int(100, 1000),
            "For_Three_Months": fake.random_int(300, 3000),
            "For_Six_Months": fake.random_int(600, 6000),
            "For_One_Year": fake.random_int(1000, 10000),
            "For_Three_Years": fake.random_int(3000, 30000)
        }
    ]),
    gross_margin=fake.random_int(100, 1000),
    net_profit=fake.random_int(100, 1000),
    cash=fake.random_int(100, 1000),
    financing_need=fake.paragraph(),
    financing_phase=fake.word(),
    remuneration_type=fake.word(),
    impactful_introduction=fake.paragraph(),
    specific_problem_addressing=fake.paragraph(),
    innovative_solution_proposal=fake.paragraph(),
    team_presentation=fake.paragraph(),
    startup_costs_explanation=fake.paragraph(),
    necessary_capital_explanation=fake.paragraph(),
    expected_revenue_explanation=fake.paragraph(),
    investment_return_demonstration=fake.paragraph(),
    investment_repayment=fake.paragraph(),
    periodic_profit_percentage=fake.paragraph(),
    economic_structural_transformation=fake.paragraph(),
    capital_wellbeing_development=fake.paragraph(),
    employment_promotion_economic_insertion=fake.paragraph(),
    governance_decentralization_strategic_state_management=fake.paragraph()
)

    db.session.add(solution)
    db.session.commit()



@solutions.route("/thousand_solution", methods=["POST"])
def thousand_solution():
    for _ in range(1000):
        faker_solution()
    return jsonify(message = "les 1000 solutions ont été enregistré")




# Route pour créer une nouvelle solution
@solutions.route('/add', methods=['POST'])
def create_solution():
    data = request.json
    new_solution = Solution(
        title=data['title'],
        problem_id=data['problem_id'],
        account_id=data['account_id'],
        description=data['description'],
        # Assurez-vous de définir les autres champs requis ici
    )
    db.session.add(new_solution)
    db.session.commit()
    return jsonify({'message': 'Solution créée avec succès'}), 201

# Route pour obtenir toutes les solutions
@solutions.route('/all', methods=['GET'])
def get_all_solutions():
    solutions = Solution.query.all()
    return jsonify([solution.serialize() for solution in solutions]), 200

# Route pour obtenir une solution spécifique par son ID
@solutions.route('/get/<int:solution_id>', methods=['GET'])
def get_solution(solution_id):
    solution = Solution.query.get(solution_id)
    if not solution:
        return jsonify({'message': 'Solution non trouvée'}), 404
    return jsonify(solution.serialize()), 200

# Route pour mettre à jour une solution existante
@solutions.route('/update/<int:solution_id>', methods=['PUT'])
def update_solution(solution_id):
    solution = Solution.query.get(solution_id)
    if not solution:
        return jsonify({'message': 'Solution non trouvée'}), 404
    data = request.json
    solution.title = data.get('title', solution.title)
    solution.description = data.get('description', solution.description)
    # Mettez à jour les autres champs au besoin
    db.session.commit()
    return jsonify({'message': 'Solution mise à jour avec succès'}), 200

# Route pour supprimer une solution existante
@solutions.route('/delete/<int:solution_id>', methods=['DELETE'])
def delete_solution(solution_id):
    solution = Solution.query.get(solution_id)
    if not solution:
        return jsonify({'message': 'Solution non trouvée'}), 404
    db.session.delete(solution)
    db.session.commit()
    return jsonify({'message': 'Solution supprimée avec succès'}), 200

