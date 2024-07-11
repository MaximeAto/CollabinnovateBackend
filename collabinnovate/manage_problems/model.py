from datetime import datetime
import random

from collabinnovate import db


class Problem(db.Model):
    __tablename__ = "problems"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    about_problem = db.Column(db.Text, nullable=False)
    country = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    dateAdded = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    activity_requiring_improvement = db.Column(db.Text, nullable=True)
    affected_population = db.Column(db.Text, nullable=True)
    concerns_of_affected_population = db.Column(db.Text, nullable=True)
    impact_on_affected_population = db.Column(db.Text, nullable=True)
    quantitative_volume_affected_population = db.Column(db.Integer, nullable=True)
    participations = db.Column(db.Integer, default = 0)

    solutions = db.relationship('Solution', backref='problems',lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'account_id': self.account_id,
            'author' : self.author,
            'title': self.title,
            'about_problem': self.about_problem,
            'country': self.country,
            'city': self.city,
            'category': self.category,
            'deadline': self.deadline.isoformat() if self.deadline else None,
            'dateAdded': self.dateAdded.isoformat() if self.dateAdded else None,
            'activity_requiring_improvement': self.activity_requiring_improvement,
            'affected_population': self.affected_population,
            'concerns_of_affected_population': self.concerns_of_affected_population,
            'impact_on_affected_population': self.impact_on_affected_population,
            'quantitative_volume_affected_population': self.quantitative_volume_affected_population,
            'participations' : self.participations
        }
