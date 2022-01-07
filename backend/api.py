import time
from flask import Flask, request
from intersg import main as m1
from linkedin import search as m2

app = Flask(__name__)

@app.route('/')
def test():
    return {'name': "server is up and running"}

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/internsg/keyword')
def get_data_internsg():
    return m1("keyword")

@app.route('/linkedin/<id>')
def get_data_linkedin(id):
    return m2(id)

print("hi")
