from collabinnovate import create_app
from flask import Blueprint, jsonify, make_response, request, current_app


app = create_app()

@app.route('/')
def hello_world():

  return jsonify({"message":request.cookies.get('codeping')})


if __name__ == '__main__':
  
  app.run(debug=True)