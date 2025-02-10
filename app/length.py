from app import app
from flask import render_template
import pint
ureg = pint.UnitRegistry()
allowed_units={
"length":["millimeter","centimeter","meter","kilometer","inch","foot","yard","mile"]}
def is_conversion_allowed(from_unit,to_unit):
    for i in allowed_units.values():
        if from_unit in i and to_unit in i:
            return True
        return False
def convert_units(value,from_unit,to_unit):
    if