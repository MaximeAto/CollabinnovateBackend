
from datetime import datetime, timedelta
import random
import re

from flask import Blueprint, jsonify, make_response, request
import jwt
from collabinnovate import db
from collabinnovate.config import SECRET_JWT_KEY
from collabinnovate.manage_user_accounts.notification.utils import confirmation_mail
from collabinnovate.manage_user_accounts.user.model import User
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/resendvalidation', methods=['GET'])
def resendvalidation():

    refresh_token = refresh_token()
    codeping = generer_code_pin()
    confirmation_mail(refresh_token.email, codeping)
    response = make_response(jsonify({'message': 'Token are been refreshed', 'user_id': refresh_token.email}), 200)
    response.set_cookie('token', refresh_token.refresh_token)
    response.set_cookie('codeping', codeping)
    
    return jsonify({'message': codeping})

@auth.route('/emailconfirmation/<codeping>', methods=['GET'])
def confirmMail(codeping):
    try:
        # Récupérer le codeping et le token JWT depuis les cookies
        cookie_codeping = request.cookies.get('codeping')
        token = request.cookies.get('token')

        # Vérifier si le codeping fourni correspond à celui stocké dans les cookies
        if codeping != cookie_codeping:
            return jsonify({'message': "Incorect code"}), 400

        # Décoder le token JWT pour vérifier sa validité
        decoded_token = jwt.decode(token, SECRET_JWT_KEY, algorithms=['HS256'])

        # Vérifier si le token JWT est encore valide
        if datetime.utcnow() > datetime.fromtimestamp(decoded_token['exp']):
            return jsonify({'message': 'Expired token.'}), 401

        return jsonify({'message': 'Codeping and token validated successfully.'}), 200

    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Expired token.'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token.'}), 401
    except Exception as e:
        return jsonify({'message': f'An error occurred: {str(e)}'}), 500

@auth.route('/login', methods=['POST'])
def login():
    try:
        data = request.form

        # Vérification de la présence du nom d'utilisateur et du mot de passe
        username = data['username']
        password = data['password']
        if not username or not password:
            return jsonify({'message' :'Username and password are required.'})

        # Vérification si l'utilisateur existe
        user = User.query.filter_by(email=username).first()
        if not user:
            return jsonify({'message' :'User not found.'})
            

        # Vérification du mot de passe
        if not check_password_hash(user.password, password):
            return jsonify({'message' :'Incorrect password.'})

        # Authentification réussie
        # implémentation la logique de création de jeton JWT ou de session utilisateur
        return jsonify({'message': 'Login successful.'}), 200

    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': 'An error occurred.', 'error': str(e)}), 500

@auth.route('/logout', methods=['POST'])
def logout():
    # implémentation la logique de déconnexion, comme la suppression de la session utilisateur
    return jsonify({'message': 'Logout successful.'}), 200

@auth.route('/refreshtoken/<email>', methods=['GET'])
def refresh_token(email):
    refreshed_token = generate_token(email)
    return {'refresh_token' : refreshed_token, 'email' : email}

def generer_code_pin():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])

def generate_token(email):
    token_payload = {
      'user_id': email,
      'exp': datetime.utcnow() + timedelta(hours=24)
    }
    token = jwt.encode(token_payload, SECRET_JWT_KEY, algorithm='HS256')

    return token




