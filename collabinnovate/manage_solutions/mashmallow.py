from collabinnovate import ma
from collabinnovate.manage_problems.model import Problem

class MashmallowProblem(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Problem