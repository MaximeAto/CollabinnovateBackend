from collabinnovate import ma
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from collabinnovate.manage_problems.model import Problem
from collabinnovate.manage_solutions.model import Solution
from collabinnovate.manage_user_accounts.account.model import Account

class MashmallowAccount(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Account
    
class MashmallowProblem(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Problem
    
class MashmallowSolution(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Solution