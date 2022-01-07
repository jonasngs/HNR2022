import time
from flask import Flask, request, json
from flask.helpers import send_from_directory
from internsg import main as m1
from linkedin import search as m2
from glints import search as m3
from flask_cors import CORS, cross_origin


app = Flask(__name__, static_folder="frontend/build", static_url_path="")
cors = CORS(app)

#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')
# def test():
#     return {'name': "server is up and running"}

@app.route('/time')
@cross_origin()
def get_current_time():
    return {'time': time.time()}

@app.route('/internsg/<keyword>')
@cross_origin()
def get_data_internsg(keyword):
    return m1(keyword)

@app.route('/linkedin/<id>')
@cross_origin()
def get_data_linkedin(id):
    return m2(id)

@app.route('/glints')
@cross_origin()
def get_data_glints():
    return m3()

@app.route('/search/<keyword>')
@cross_origin()
def search(keyword):
    result = []
    # call your method and append it to result
    #linkedin = m2(keyword)
    glints = m3(keyword)
    internsg = m1(keyword)
    #result.append(json.loads(linkedin))
    result.append(json.loads(glints))
    result.append(json.loads(internsg))

    return json.dumps(result)
# deploy to heroku
# git subtree push --prefix backend heroku master


