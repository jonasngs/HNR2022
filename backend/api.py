import time
from flask import Flask, request, json
from intersg import main as m1
from linkedin import search as m2
from glints import main as m3

app = Flask(__name__)

@app.route('/')
def test():
    return {'name': "server is up and running"}

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/internsg')
def get_data_internsg():
    return m1()

@app.route('/linkedin/<id>')
def get_data_linkedin(id):
    return m2(id)

@app.route('/glints')
def get_data_glints():
    return m3()

@app.route('/search/<keyword>')
def search(keyword):
    result = []
    linkedin = m2(keyword)
    result.append(json.loads(linkedin))
    return json.dumps(result)

