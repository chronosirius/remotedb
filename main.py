from flask import Flask
from os import environ

app = Flask(__name__)

@app.route('/')
def index():
  with open('save.json') as f:
    return f.read(), 200

@app.route('/update', methods=['POST'])
def update():
  with open('save.json', 'w') as f:
    f.write(request.form['new'])
  return "", 200
  
app.run('0.0.0.0', int(environ.get('PORT', 80)))
