import pymongo

client = pymongo.MongoClient("mongodb+srv://santoshsingh:MTZUCJZJr8Lr6aV@cluster0.0qmop3i.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"santosh",
    "email":"santosh@uber.com",
    "surname":"singh"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

