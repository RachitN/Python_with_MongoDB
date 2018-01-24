import pymongo
uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['mycustomers']
collection = database['customers']
collection.insert({"first_name":"hey","last_name":"bro"})
students = collection.find({})
for student in students:
    print(student)

