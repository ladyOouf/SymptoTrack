# Prologue Comments
# • Name of code artifact: models.py
# • Description: creates the user session
# • Programmer’s name: Sarah Martinez
# • Data of Creation: 01.25.2023
# • Latest Revision: 02.11.2024
# • Brief description of each revision & author
# • Preconditions: Requires my password and username created on MongoDb in order to access the cluster
#   Username/Password are hidden and not shown. .ENV contains MongoDB URI. IP must be added to Database Cluster
#   Query setup: { field: 'value' }
# • Postconditions: None
# • Errors: login error occurs please check faults
# • Side effects: None
# • Invariants: None
# • Any known faults: the entire folder doesn't seem to work in the actual repo, but it works separately.

from flask import Flask, jsonify, request, session, redirect, url_for
from passlib.hash import pbkdf2_sha256
from app import db
import uuid


class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):

        print(request.form)

        # CREATE THE USER OBJECT
        user = {
            "_id": uuid.uuid4().hex,
            "firstName": request.form['firstName'],
            "lastName": request.form['lastName'],
            "email": request.form['email'],
            "password": request.form['password']
        }
        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Check for existing email address
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email address already in use"}), 400

        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):

        user = db.users.find_one({
            "email": request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)

        return jsonify({"error": "Invalid login credentials"}), 401



class PainLog:

    def log_pain(self):
        user_id = session['user']['_id']
        pain_input = int(request.form['pain_input'])
        pain_date = datetime.datetime.strptime(request.form['pain_date'], '%Y-%m-%d').date()
        pain_description = request.form['pain_description']

        pain_log_entry = {
            "user_id": user_id,
            "pain_input": pain_input,
            "pain_date": pain_date,
            "pain_description": pain_description
        }

        # Insert the pain log entry into the database
        db.pain.insert_one(pain_log_entry)

        return jsonify({"message": "Pain log entry recorded successfully"}), 200
