#!/usr/bin/env python3
"""
update  school names by topic
"""

import pymongo

def update_topics(mongo_collection, name, topics):
 client = MongoClient()
    db = client['database_name']
    collection = db['schools']
    collection.update_many(
        {'name': mongo_collection},
        {'$set': {'topics': topics}}
    )
    client.close()
