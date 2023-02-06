import pymongo


from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

post_db = client.post_database
post_collection = post_db.post_collection
