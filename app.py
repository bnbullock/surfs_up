from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/About')
def about_helloworld():
    return 'Hello World is a Test Application'