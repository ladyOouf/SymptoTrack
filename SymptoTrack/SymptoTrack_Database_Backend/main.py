# Prologue Comments
# • Name of code artifact: SymptoTrack_Database_Backend
# • Description: Establishes signal to MongoDb Cluster and Sample Collections. The code has sample lines to explain what
#  each section does. These sections are mainly being used as a reference and will not be used for the website's code.
# • Programmer’s name: Sarah Martinez
# • Data of Creation: 10.22.2023
# • Latest Revision: 10.22.2023
# • Brief description of each revision & author
# • Preconditions: Requires my password and username created on MongoDb in order to access the cluster
#   Username/Password are hidden and not shown. .ENV contains MongoDB URI. IP must be added to Database Cluster
#   Query setup: { field: 'value' }
# • Postconditions: Currently in this code, I used a sample set collection on MongoDB to test out the pymongo package
# • Return values: Depends on the query request
# • Errors: No current errors unless document doesn't exist
# • Side effects: None
# • Invariants: None
# • Any known faults: None

import os

from pprint import pprint
import bson
from datetime import datetime
from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)


# Sends a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# List all the databases in the cluster:
for db_info in client.list_database_names():
    print(db_info)

# # Get a reference to the 'sample_mflix' database:
# db = client['sample_mflix']
#
# # List all the collections in 'sample_mflix':
# collections = db.list_collection_names()
# for collection in collections:
#     print(collection)
#
# # Get a reference to the 'movies' collection:
# movies = db['movies']
#
# # Get the document with the title 'Blacksmith Scene':
# pprint(movies.find_one({'title': 'The Great Train Robbery'}))
#
# # Insert a document for the movie 'Parasite':
# insert_result = movies.insert_one({
#     "title": "Parasite",
#     "year": 2020,
#     "plot": "A poor family, the Kims, con their way into becoming the servants of a rich family, the Parks.",
#     "released": datetime(2020, 2, 7, 0, 0, 0),
# })
#
# # Save the inserted_id of the document you just created:
# parasite_id = insert_result.inserted_id
# print("_id of inserted document: {parasite_id}".format(parasite_id=parasite_id))
# print(movies.find_one({'_id': bson.ObjectId(parasite_id)}))
#
# # Look up the documents you've created in the collection:
# for doc in movies.find({"title": "Parasite"}):
#     pprint(doc)
#
# # Update all the Parasite movie docs to the correct year:
# update_result = movies.update_many({"title": "Parasite"}, {"$set": {"year": 2019}})
# # # Update the document with the correct year:
#
# # Print out the updated record to make sure it's correct:
# pprint(movies.find_one({'_id': bson.ObjectId(parasite_id)}))
#
# # Deletes all entries titled 'Parasite':
# movies.delete_many({"title": "Parasite"})
