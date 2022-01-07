import time
from flask import Flask, request, json
from internsg import main as m1
from linkedin import search as m2
from glints import search as m3
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def test():
    return {'name': "server is up and running"}

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/internsg/<keyword>')
def get_data_internsg(keyword):
    return m1(keyword)

@app.route('/linkedin/<id>')
def get_data_linkedin(id):
    return m2(id)

@app.route('/glints')
def get_data_glints():
    return m3()

@app.route('/search/<keyword>')
def search(keyword):
    result = []
    # call your method and append it to result
    linkedin = m2(keyword)
    glints = m3(keyword)
    internsg = m1(keyword)
    result.append(json.loads(linkedin))
    result.append(json.loads(glints))
    result.append(json.loads(internsg))

    return json.dumps(result)


