from flask import Flask
from flask import render_template
from flask import request

login = Flask(__name__)

@login.route('/')
def index():
    return render_template('index.html')

@login.route('/myRequest', methods=['GET', 'POST'])
def parse_request():
    if request.method == 'GET':
        fname = request.args['fname']
    return ' <h1> result is ' +  fname  +' </h1> '
 
    

if __name__ == '__main__':
    login.run()
