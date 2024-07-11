from collabinnovate import create_app
from flask import Blueprint, jsonify, make_response, request, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

app = create_app()

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(message=current_user), 200


if __name__ == '__main__':
  
  app.run(debug=True)