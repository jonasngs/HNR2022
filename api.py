import time
from flask import Flask, request, json
from flask.helpers import send_from_directory
from internsg import main as m1
from linkedin import search as m2
from glints import search as m3
from flask_cors import CORS, cross_origin
import multiprocessing
from multiprocessing import *


app = Flask(__name__, static_folder="frontend/build", static_url_path="")
cors = CORS(app)

#app.config['CORS_HEADERS'] = 'Content-Type'

# @app.route('/')
# @cross_origin()
# def serve():
#     return send_from_directory(app.static_folder, 'index.html')

@app.route("/")
def index():
    return "Hello World!"

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

def linkedin(keyword, sharedList):
    print("LinkedIn")
    linkedin = m2(keyword)
    sharedList.extend(json.loads(linkedin))

def glints(keyword, sharedList):
    print("Glints")
    glints = m3(keyword)
    sharedList.extend(json.loads(glints))

def internsg(keyword, sharedList):
    print("InternSg")
    internsg = m1(keyword)
    sharedList.extend(json.loads(internsg))

@app.route('/search/<keyword>')
def search(keyword):
    manager = Manager()
    result = manager.list()
    process = []
    for i in range(0, 3):
        if i == 0:
            p = Process(target=linkedin, args=(keyword, result))
        if i == 1:
            p = Process(target=internsg, args=(keyword, result))
        if i == 2:
            p = Process(target=glints, args=(keyword, result))
        process.append(p)
        p.start()
    for i in process:
        i.join()

    # call your method and append it to result
    # print(result)
    result = list(result)
    return json.dumps(result)
# deploy to heroku
# git subtree push --prefix backend heroku master


