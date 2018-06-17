from flask import Flask, render_template, request, jsonify



Server = Flask(__name__)

@Server.route('/', methods = ['GET','POST'])
def index():
    value = request.json['key']
@Server.route('/about')
def about():
    return "Hello world"

if __name__ == "__main__":
    Server.run()
