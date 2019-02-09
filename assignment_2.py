import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()
db = client.socialnetDB
tweets = db.tweets


def pp(obj):
    pprint.pprint(obj)

def ppall(col):
    for p in col:
        pp( p )

def user_count():
 pp(len(tweets.distinct('user')))

def user_linking_themost():
    ppall(db.tweets.aggregate([
        {
        '$match': {
            'text': {
                '$regex': "@"
            }
        }
        },
        {
        '$group': {
            '_id': '$user',
            'count': {
                '$sum': 1
                }
        }
        },
        {
        '$sort': {
            'count': -1
        }
        },
        {
        '$limit': 10
        }
    ]))

def most_mentioned_users():
    ppall(db.tweets.aggregate([
        {
        '$group': {
            '_id': '$user',
            'count': {
                '$sum': 1
                }
        }
        },
        {
        '$sort': {
            'count': -1
        }
        },
        {
        '$limit': 10
        }
    ]))

def most_negative_tweets():
    ppall(db.tweets.aggregate([
        {
        '$match': {
            'polarity': 0
        }
        },
        {
        '$group': {
            '_id': '$text',
        }
        },
        {
        '$sort': {
            'count': -1
        }
        },
        {
        '$limit': 5
        }
    ]))

def most_positive_tweets():
    ppall(db.tweets.aggregate([
        {
        '$match': {
            'polarity': 4
        }
        },
        {
        '$group': {
            '_id': '$text',
        }
        },
        {
        '$sort': {
            'count': -1
        }
        },
        {
        '$limit': 5
        }
    ]))

user_count()
print("---------")
user_linking_themost()
print("---------")
most_mentioned_users()
print("---------")
most_negative_tweets()
print("---------")
most_positive_tweets()
