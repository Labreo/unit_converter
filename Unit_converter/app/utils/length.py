import pint

ureg = pint.UnitRegistry()

allowed_units = {
    "length": ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"],
    "weight": ["gram", "kilogram", "pound", "ounce"],
    "temperature": ["celsius", "fahrenheit", "kelvin"]
}


def is_conversion_allowed(from_unit, to_unit):
    for units in allowed_units.values():
        if from_unit in units and to_unit in units:
            return True
    return False


def convert_units(value, from_unit, to_unit):
    try:
        value = float(value)

        # Handle Temperature Separately
        if from_unit in allowed_units["temperature"] and to_unit in allowed_units["temperature"]:
            if from_unit == "celsius" and to_unit == "fahrenheit":
                return (value * 9 / 5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                return (value - 32) * 5 / 9
            elif from_unit == "celsius" and to_unit == "kelvin":
                return value + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                return value - 273.15
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                return (value - 32) * 5 / 9 + 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                return (value - 273.15) * 9 / 5 + 32
            else:
                return "Invalid temperature conversion"

        # Other conversions (length, weight)
        if is_conversion_allowed(from_unit, to_unit):
            from_quantity = value * ureg(from_unit)
            return from_quantity.to(to_unit).magnitude

        return "Conversion not allowed"

    except pint.errors.DimensionalityError:
        return "Incompatible unit conversion"
    except Exception as e:
        return f"Error: {e}"




