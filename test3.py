import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://santosh:Mongo_123@cluster0.8fq9ih3.mongodb.net/?retryWrites=true&w=majority")
db = client.test

""" use this file to perform the search and other operations on MongoDB """