from connect import *

db = client.testdb

x = db.reviews.delete_many({"rating": 1})
print(x.deleted_count)