from sqlalchemy import JSON
from collabinnovate import db

class Account(db.Model):
    __tablename__ = "accounts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type_account = db.Column(db.String(50), nullable=False)
    account_details = db.Column(JSON)
    role = db.Column(db.String(50), nullable=False)
    
    
    # Relations with other tables
    solutions = db.relationship('Solution', backref='accounts')
    problems = db.relationship('Problem', backref='accounts')
    

  