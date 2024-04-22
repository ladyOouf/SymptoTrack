# Prologue Comments
# • Name of code artifact: models.py
# • Description: creates the user session
# • Programmer’s name: Sarah Martinez
# • Data of Creation: 01.25.2023
# • Latest Revision: 04.07.2024
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
from database import db
import datetime
from bson import ObjectId


import uuid


class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):

        print(request.form)

        user = {
            "_id": uuid.uuid4().hex,
            "firstName": request.form['firstName'],
            "lastName": request.form['lastName'],
            "email": request.form['email'],
            "password": request.form['password']
        }

        user['password'] = pbkdf2_sha256.encrypt(user['password'])

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
            "email": request.form['email']
        })

        if user and pbkdf2_sha256.verify(request.form['password'], user['password']):
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
            "pain_date": str(pain_date),
            "pain_description": pain_description
        }
        print("Received pain_input:", pain_input)
        db.pain.insert_one(pain_log_entry)

        return jsonify({"message": "Pain log entry recorded successfully"}), 200

    def get_pain_logs(self, user_id):
        return db.pain.find({"user_id": user_id})


class Journal:

    def journal_input(self):
        user_id = session['user']['_id']
        weather = request.form['weather']
        journal_date = datetime.datetime.strptime(request.form['journal_date'], '%Y-%m-%d').date()
        mood = request.form['mood']
        grateful = request.form['grateful']
        goals = request.form['goals']
        notes = request.form['notes']
        tomorrow = request.form['tomorrow']

        journal_entry = {
            "user_id": user_id,
            "journal_date": str(journal_date),
            "weather": weather,
            "mood": mood,
            "grateful": grateful,
            "goals": goals,
            "notes": notes,
            "tomorrow": tomorrow,

        }
        print("Received mood:", mood)
        db.journal.insert_one(journal_entry)

        return jsonify({"message": "Journal log entry recorded successfully"}), 200

    def get_journal_entries(self, user_id, selected_date):
        return db.journal.find({"user_id": user_id, "journal_date": selected_date})


class Medslist:

    def med_input(self):
        user_id = session['user']['_id']
        GenericName = request.form['GenericName']
        Strength = request.form['Strength']
        MedicationForm = request.form['MedicationForm']
        DosingSchedule = request.form['DosingSchedule']
        Instruction = request.form['Instruction']

        med_log_entry = {
            "user_id": user_id,
            # "brandName": brandName,
            "GenericName": GenericName,
            "Strength": Strength,
            "MedicationForm": MedicationForm,
            "DosingSchedule": DosingSchedule,
            "Instruction": Instruction,
        }
        print("Received Meds:", Strength )
        db.meds.insert_one(med_log_entry)

        return jsonify({"message": "Med entry recorded successfully"}), 200

    def get_meds(self, user_id):
        return db.meds.find({"user_id": user_id})

    def find_one(self, med_id):
        return db.meds.find_one({'_id': ObjectId(med_id)})


class Result:
    def result_input(self):
        user_id = session['user']['_id']
        result_date = datetime.datetime.strptime(request.form['Date'], '%Y-%m-%d').date()
        results = request.form.get('totalPoints')

        result_entry = {
            "user_id": user_id,
            "Date": str(result_date),
            "totalPoints": results,

        }
        print("Received results:", results )
        db.pain_results.insert_one(result_entry)

        return jsonify({"message": "results entry recorded successfully"}), 200

    def get_results(self, user_id):
        return db.pain_results.find({"user_id": user_id})
