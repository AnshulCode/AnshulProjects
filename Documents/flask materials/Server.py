from flask import Flask, render_template, request, jsonify
import twilioApp

Server = Flask(__name__)

@Server.route('/index', methods = ['GET','POST'])
def index():
    twilioApp.sendSMS("hello world")
    return "message sent"

@Server.route('/about')
def about():
    return "Hello world"



