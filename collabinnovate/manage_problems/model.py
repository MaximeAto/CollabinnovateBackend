import random

from collabinnovate import db


class Problem(db.Model):
    __tablename__ = "problems"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    about_problem = db.Column(db.Text, nullable=False)
    country = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    activity_requiring_improvement = db.Column(db.Text, nullable=True)
    affected_population = db.Column(db.Text, nullable=True)
    concerns_of_affected_population = db.Column(db.Text, nullable=True)
    impact_on_affected_population = db.Column(db.Text, nullable=True)
    quantitative_volume_affected_population = db.Column(db.Integer, nullable=True)

    solutions = db.relationship('Solution', backref='problems')

