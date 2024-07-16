from collabinnovate import create_app
from flask import Blueprint, jsonify, make_response, request, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

app = create_app()

@app.route('/', methods=['GET'])
def root():
    return jsonify({"message": "good job"})


if __name__ == '__main__':
  
  app.run(debug=True)