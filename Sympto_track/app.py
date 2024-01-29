
from flask import Flask, render_template, session, flash, redirect, url_for
from functools import wraps
from pymongo import MongoClient

from dotenv import load_dotenv
import os

# Database
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)
db = client['symptotrack']
users = db['user_creds']


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            flash('You need to login first')
            return redirect('/')
    return wrap

#routes
from user import routes


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup/')
def register():
    return render_template('Sign up.html')


@app.route('/homepage/')
@login_required
def perfil():
    return render_template('Homepage.html')
