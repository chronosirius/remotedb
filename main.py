from flask import Flask, request
from os import environ

app = Flask(__name__)

@app.route('/')
def index():
  try:
    with open('save.json') as f:
      return f.read(), 200
  except:
    return "", 200

@app.route('/update', methods=['POST'])
def update():
  if request.form('password') == environ['password']:
    with open('save.json', 'w') as f:
      f.write(request.form['new'])
    return "", 200
  else:
    return "", 401
  
app.run('0.0.0.0', int(environ.get('PORT', 80)))
