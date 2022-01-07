import time
from flask import Flask
from intersg import main as m1

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

print("hi")
