from app import app
from flask import render_template,request
from app.utils.length import convert_units
allowed_units = {
    "length": ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"],
    "weight": ["gram", "kilogram", "pound", "ounce", "ton"],
    "temperature": ["celsius", "fahrenheit", "kelvin"]
}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/length', methods=["GET", "POST"])
def length():
    result = None
    if request.method == "POST":
        value = request.form["value"]
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        result = convert_units(value, from_unit, to_unit)
    return render_template("length.html", result=result, units=allowed_units["length"])

@app.route('/weight', methods=["GET", "POST"])
def weight():
    result = None
    if request.method == "POST":
        value = request.form["value"]
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        result = convert_units(value, from_unit, to_unit)
    return render_template('weight.html', result=result, units=allowed_units["weight"])
@app.route('/temperature',methods=["GET", "POST"])
def temperature():
    result = None
    if request.method == "POST":
        value = request.form["value"]
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        result = convert_units(value, from_unit, to_unit)
    return render_template('temperature.html', result=result, units=allowed_units["temperature"])
