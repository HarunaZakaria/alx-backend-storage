#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""
def list_all(mongo_collection):
    cursor = mongo_collection.find({})
    docs = list(cursor)
    if len(docs) == 0:
        print('No documents found in collection')
        return []
    else:
        for doc in docs:
            print(doc)
        return docs
