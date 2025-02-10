from app import app
from flask import render_template
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')
@app.route('/length')
def length():
    return render_template('length.html',title='Length')
@app.route('/weight')
def weight():
    return render_template('weight.html',title='Weight')
@app.route('/temperature')
def temperature():
    return render_template('temperature.html',title='Temperature')