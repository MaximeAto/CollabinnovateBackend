from flask import Blueprint


roles = Blueprint('roles', __name__)

@roles.route('/get/<int:role_id>', methods=['GET'])
def get_role(role_id):
  pass

@roles.route('/create', methods=['POST'])
def create_role():
  pass

@roles.route('/update/<int:role_id>', methods=['PUT'])
def update_role(role_id):
  pass

@roles.route('/delete/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
  pass
