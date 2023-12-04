# • Programmer’s name: Sarah Martinez
# • Data of Creation: 10.22.2023
# • Latest Revision: 12.03.2023
# • Brief description of each revision & author
# • Preconditions: Requires my password and username created on MongoDb in order to access the cluster
#   Username/Password are hidden and not shown. .ENV contains MongoDB URI. IP must be added to Database Cluster
#   Query setup: { field: 'value' }
# • Postconditions: None
# • Errors: login error occurs please check faults
# • Side effects: None
# • Invariants: None
# • Any known faults: revamping the entire set up the site, the script.js and jqueries are sending status codes 500 and
# 404, regardless of what I've done, I can't remove it and it's likely due to the set up the files and the script.js,
# this will be updated with the routes from main.py once I can for sure make the practice project Im using work

from SymptoTrack.SymptoTrack_Database_Backend import app
from SymptoTrack.SymptoTrack_Database_Backend.users.models import User


@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()


@app.route('/user/signout')
def signout():
    return User().signout()


@app.route('/user/login', methods=['POST'])
def login():
    return User().login()
