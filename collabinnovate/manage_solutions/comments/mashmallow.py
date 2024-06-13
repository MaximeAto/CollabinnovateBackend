from collabinnovate import ma
from collabinnovate.manage_solutions.comments import Comment

class MashmallowProblem(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Comment