from flask_mail import Message
from flask import render_template,current_app
from collabinnovate import mail


def confirmation_mail(mail,codeping):
  msg = Message('MAIL DE CONFIRMATION', 
                sender='melainenkeng@gmail.com',
                recipients=[mail])
  msg.html = render_template('confirmMail.html', codeping = codeping)


def welcome_mail(full_name, email):
  msg = Message('Welcome to Collabinnovate', 
                sender='melainenkeng@gmail.com',
                recipients=[email])
  msg.html = render_template('welcome.html', full_name = full_name)
  
  mail.send(msg)