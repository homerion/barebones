#need to import app variable
from app import app
#if you want to render html
from flask import render_template



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
