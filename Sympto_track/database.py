# <!--Name of Code artifact: pain_chart.html
# Description: This code is to initialize the database
# Authors: Sarah M
# Date Creation : March 24, 2024
# Date Revised: March 24, 2024
# Preconditions: Empty Strings are not allowed.
# Postconditions: No return values. -->

from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

client = MongoClient(MONGODB_URI)
db = client['symptotrack']
users = db['user_creds']
symptoms = db['pain']
