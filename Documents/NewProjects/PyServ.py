from flask import Flask, render_template, request, jsonify

PyServ = Flask(__name__)

@PyServ.route('/')
def index():
    return "INDEX"


if __name__ == '__main__' :
    PyServ.run()