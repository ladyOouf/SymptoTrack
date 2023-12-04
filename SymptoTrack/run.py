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
# 404, regardless of what I've done, I can't remove it and it's likely due to the set up the files and the script.js

from flask import render_template, session
# from flaskapp import app, login_required
from SymptoTrack_Database_Backend.main import *

app.template_folder = "../templates"
app.static_folder = "../static"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/homepage')
def homepage():
    return render_template('Homepage.html')


if __name__ == '__main__':
    app.run(debug=True)
