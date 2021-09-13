from pymongo import MongoClient

url = "mongodb+srv://admin:root@cluster0.yddkv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.testdb