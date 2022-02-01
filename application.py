from flask import Flask, render_template, jsonify
from markupsafe import re


application = Flask(__name__)

@application.route('/')
def index():
    return render_template("index.html")

@application.route('/about')
def about():
    return render_template("about.html")

@application.route('/contact')
def contact():
    return render_template("contact.html")

@application.route('/projects')
def projects():
    return render_template("projects.html")

@application.route('/time')
def time():
    return render_template("time.html")

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=3000)