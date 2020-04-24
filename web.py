import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloIndex():
    return 'Hello World from Python Flask!'

@app.route('/food')
def foodIndex():
    return 'Hungry?'

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

app.run(host='0.0.0.0', port=5000)
