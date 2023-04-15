#!/usr/bin/env python3
"""
update  school names by topic
"""

import pymongo

def update_topics(mongo_collection, name, topics):
 return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
