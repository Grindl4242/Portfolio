from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client["Portfolio_db"]
collection = db["Projects"]

f = open('test_values.json', 'r')
data = eval(f.read())

collection.drop()
collection.insert_many(data)
