from collabinnovate import db
from collabinnovate.manage_user_accounts.class_for_manyTomany.group_membership import group_membership

class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  full_name = db.Column(db.String(100))
  cover = db.Column(db.String(100))
  email = db.Column(db.String(100), unique=True, nullable=False)
  phone_number = db.Column(db.String(20), unique=True)
  social_link = db.Column(db.String(100))
  password = db.Column(db.String(100), nullable=False)
  address = db.Column(db.String(100))
  city = db.Column(db.String(100))
  country = db.Column(db.String(100))
  profile_photo = db.Column(db.String(100))
  bio = db.Column(db.Text)
  activity_domain = db.Column(db.String(100))
  notifications = db.Column(db.Boolean, default=True)
  group = db.Column(db.String(100))
  work_title = db.Column(db.String(100))
  website = db.Column(db.String(100))
  language = db.Column(db.String(50))
  confirmed = db.Column(db.Boolean, default= False)


  accounts = db.relationship('Account', backref = 'users',uselist = False)
  notifications = db.relationship('Notification', backref = 'users')
  sessions = db.relationship('Session', backref = 'users')
  groups = db.relationship('Group', secondary=group_membership, backref='users')
  comments = db.relationship('Comment', backref='users')

  

  