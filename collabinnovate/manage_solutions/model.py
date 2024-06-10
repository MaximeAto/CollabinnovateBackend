from collabinnovate import db
from sqlalchemy import JSON
import random
import json


class Solution(db.Model):
    __tablename__ = "solutions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey('problems.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    
    # Solution information fields
    description = db.Column(db.Text, nullable=False)
    product_offered = db.Column(db.String(100))
    service_offered = db.Column(db.String(100))
    customer_expectations = db.Column(db.Text)
    what_company_sells = db.Column(db.String(100))
    how_product_service_marketed = db.Column(db.Text)
    customer_access_method = db.Column(db.String(100))

    competitors = db.Column(JSON)

    # Distribution channels fields
    direct_sales = db.Column(db.Boolean)
    direct_sales_details = db.Column(db.Text)
    wholesale = db.Column(db.Boolean)
    informal = db.Column(db.Boolean)

    # Promotion means fields
    advertising = db.Column(db.Boolean)
    direct_marketing = db.Column(db.Boolean)
    sales_promotion = db.Column(db.Boolean)
    display = db.Column(db.Boolean)
    word_of_mouth = db.Column(db.Boolean)
    trade_show = db.Column(db.Boolean)
    mail_order = db.Column(db.Boolean)

    # Human resources fields
    human_resources = db.Column(JSON)

    # Legal form field
    legal_form = db.Column(db.String(100))

    # Required investment fields
    financing_needed = db.Column(db.String(100))
    investment_characteristics = db.Column(db.Text)
    suppliers = db.Column(JSON)
    amount = db.Column(db.Float)

    # Working capital fields
    variable_cost = db.Column(db.Float)
    fixed_cost = db.Column(db.Float)

    # Financial forecast fields
    offers = db.Column(JSON)
    quantity_sold = db.Column(db.Float)
    revenue_generated = db.Column(JSON)

    # Profit generation fields
    gross_margin = db.Column(db.Float)
    net_profit = db.Column(db.Float)

    # Cash flow plan fields
    cash = db.Column(db.Float)

    # Financing need field
    financing_need = db.Column(db.Text)

    # Financing phase fields
    financing_phase = db.Column(db.String(100))

    # Financing source fields

    # Equity
    private_savings = db.Column(db.Boolean)
    private_sphere_borrowing = db.Column(db.Boolean)
    private_shareholders = db.Column(db.Boolean)
    startup_sponsors = db.Column(db.Boolean)
    business_agents = db.Column(db.Boolean)
    incubator_nursery = db.Column(db.Boolean)
    mixed_capital = db.Column(db.Boolean)

    # Credit
    bank_credit = db.Column(db.Boolean)
    startup_launch_credit = db.Column(db.Boolean)
    mezzanine_financing = db.Column(db.Boolean)

    # Public subsidy for business creation
    business_creation_aid_program = db.Column(db.Boolean)
    startup_contests = db.Column(db.Boolean)

    # Crowdfunding
    crowdfunding = db.Column(db.Boolean)
    crowd_investing = db.Column(db.Boolean)
    crowd_lending = db.Column(db.Boolean)

    # Capital provider remuneration strategy field
    remuneration_type = db.Column(db.String(100))

    # Executive summary production fields
    impactful_introduction = db.Column(db.Text)
    specific_problem_addressing = db.Column(db.Text)
    innovative_solution_proposal = db.Column(db.Text)
    team_presentation = db.Column(db.Text)
    startup_costs_explanation = db.Column(db.Text)
    necessary_capital_explanation = db.Column(db.Text)
    expected_revenue_explanation = db.Column(db.Text)
    investment_return_demonstration = db.Column(db.Text)
    investment_repayment = db.Column(db.Text)
    periodic_profit_percentage = db.Column(db.Text)

    # Strategy mobilized pillars fields
    economic_structural_transformation = db.Column(db.Text)
    capital_wellbeing_development = db.Column(db.Text)
    employment_promotion_economic_insertion = db.Column(db.Text)
    governance_decentralization_strategic_state_management = db.Column(db.Text)



