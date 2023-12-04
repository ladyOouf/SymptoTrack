# • Programmer’s name: Sarah Martinez
# • Data of Creation: 10.22.2023
# • Latest Revision: 12.03.2023
# • Brief description of each revision & author
# • Preconditions: Requires my password and username created on MongoDb in order to access the cluster
#   Username/Password are hidden and not shown. .ENV contains MongoDB URI. IP must be added to Database Cluster
#   Query setup: { field: 'value' }
# • Postconditions: None
# • Errors: script.js returns document but not actual query
# • Side effects: None
# • Invariants: None
# • Any known faults: revamping the entire set up the site, the script.js and jqueries are sending status codes 500 and
# 404, regardless of what I've done, I can't remove it and it's likely due to the set up the files and the script.js


from flask import jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from SymptoTrack.SymptoTrack_Database_Backend import db
import uuid


class User:
    def start_session(self, user):
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        print(request.form)

        # Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }
        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        if db.users.insert_one(user):
            return jsonify(user), 200