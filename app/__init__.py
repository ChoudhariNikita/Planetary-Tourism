from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysql_connector import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'  # MySQL host
app.config['MYSQL_USER'] = 'admin'  # MySQL username
app.config['MYSQL_PASSWORD'] = 'adminroot@123'  # MySQL password
app.config['MYSQL_DB'] = 'Planetary'  # Your MySQL database
mysql = MySQL(app)

# Define your routes


@app.route('/')
def index():
    return render_template('User/index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/sign_in')
# def sign_in():
#     return render_template('sign_in.html')
