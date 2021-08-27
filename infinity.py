from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "kronii-copter has landed"

def run():
  app.run(host='0.0.0.0',port=8080)

def infinity():
    t = Thread(target=run)
    t.start()