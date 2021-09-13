from connect import *
from bson.objectid import ObjectId
from random import randint

db = client.testdb

def write_to_db():
    names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
    company_type = ['LLC','Inc','Company','Corporation']
    company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']

    for x in range(10):
        business = {
            'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
            'rating' : randint(1, 5),
            'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
        }
        #Step 3: Insert business object directly into MongoDB via insert_one
        result=db.reviews.insert_one(business)
        #Step 4: Print to the console the ObjectID of the new document
        print('Created {0} of 10 as {1}'.format(x,result.inserted_id))
        #Step 5: Tell us that you are done
        print('finished creating 10 business reviews')

def read_from_db():
    # find first with rating = 2
    ans = db.reviews.find_one({"rating": 2})
    print(ans)

    # find first with _id = ''
    ans = db.reviews.find_one({"_id": ObjectId("613f43e336ea9e07cfe01b87")})
    print(ans)

    # find all with name containing 'ti' (case senstive)
    # reviews = db.reviews.find({"name":{"$regex": "ti"}})

    # find all with name ending 'tion' (case insenstive)
    reviews = db.reviews.find({"name":{"$regex": "tion$", "$options": "i"}})
    for review in reviews:
        print(review)

    reviews = db.reviews.find({"rating":{"$gt": 4}})
    for review in reviews:
        print(review)

def get_restaurants():
    val = input("Enter a rating (1-5): ")
    rating = int(val)
    reviews = db.reviews.find({"rating": rating})
    for review in reviews:
        print(review)

if __name__ == "__main__":
    # get_restaurants(rating)
    read_from_db()
