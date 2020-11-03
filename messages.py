import os
import random
import pymongo

#mongo db url
MONGO_URL = os.environ.get('DB')

#database
mongo = pymongo.MongoClient(MONGO_URL)
db = mongo.cheery

def returnRandomMessage():
    n = db.messages.count()

    randomMessage = random.randint(0,n-1)

    message = list(db.messages.find().skip(randomMessage).limit(1))
    return message[0]['message']

def addUserMessage(msg):
    db.messages.insert_one({'message': msg})