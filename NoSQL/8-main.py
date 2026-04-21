#!/usr/bin/env python3
"""Python function that lists all documents in a collection
"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """Returns a list of all documents in a collection
    Args:
        mongo_collection: The collection to list documents from
    Returns:
        A list of all documents in the collection
    """
    return list(mongo_collection.find())