from collabinnovate import db
from collabinnovate.manage_user_accounts.class_for_manyTomany.group_membership import group_membership

class Group(db.Model):
  __tablename__ = "groups"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.Text)
  # users = db.relationship('User', secondary=group_membership, backref='groups')
