from collabinnovate import db

class Role(db.Model):
  __tablename__ = "roles"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(50), unique=True, nullable=False)
  description = db.Column(db.Text)
  
