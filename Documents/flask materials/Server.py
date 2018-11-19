from flask import Flask, render_template, request, jsonify
import twilioApp

Server = Flask(__name__)

@Server.route('/', methods = ['POST'])
def index():
    twilioApp.sendSMS("hello world")
    return "message sent"

@Server.route('/about')
def about():
    return "Hello world"

if __name__ == "__main__":
    Server.run(host="0.0.0.0",ssl_context = 'adhoc')
