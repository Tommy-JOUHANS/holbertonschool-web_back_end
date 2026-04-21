#!/usr/bin/env python3
"""
a Python function that lists all documents in a collection
"""
from pymongo import mongo_collection

def list_all(mongo_collection):
    """list all documents in a collection
    Args:
        mongo_collection: the pymongo collection object
    Returns:
        list of documents in the collection
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
