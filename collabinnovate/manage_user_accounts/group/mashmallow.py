from collabinnovate import ma
from collabinnovate.manage_user_accounts.group.model import Group
from collabinnovate.manage_user_accounts.user.model import User

class MashmallowUser(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = User
    

class MashmallowGroup(ma.SQLAlchemyAutoSchema):
  users = ma.Nested(MashmallowUser,many=True)
  class Meta:
    model = Group