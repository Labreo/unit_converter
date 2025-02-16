Unit Converter

This is a Flask-based web application that allows users to convert between different units of length, weight, and temperature.

Features

Convert between multiple units of length, weight, and temperature.

Simple and elegant UI with a responsive design.

Flask-based backend for handling unit conversions.

Uses Jinja templates for dynamic rendering.

Installation

Prerequisites

Python 3.x

Flask

Pint (for unit conversions)

Setup

Clone the repository:

git clone https://github.com/Labreo/unit-converter.git
cd unit-converter

Create a virtual environment:

python -m venv .venv

Activate the virtual environment:

On Windows:

.venv\Scripts\activate

On macOS/Linux:

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Usage

Run the Flask app:

python run.py

Open your browser and go to:

http://127.0.0.1:5000

Select a category (Length, Weight, Temperature) and perform conversions.

Project Structure

unit-converter/
│── app/
│   ├── templates/          # HTML templates
│   ├── static/             # CSS & JS files
│   ├── routes.py           # Flask routes
│   ├── converter.py        # Conversion logic
│   ├── __init__.py         # App initialization
│── run.py                  # Entry point for running the app
│── requirements.txt         # Dependencies
│── README.md               # Project documentation

Routes

/ - Home page

/length - Length conversion page

/weight - Weight conversion page

/temperature - Temperature conversion page

Issues & Contributions

Feel free to submit issues or contribute by forking the repository and submitting a pull request.

License

This project is licensed under the MIT License.

