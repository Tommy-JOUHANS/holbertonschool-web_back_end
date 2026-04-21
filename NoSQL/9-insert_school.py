#!/usr/bin/env python3
"""Python function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs
    Args:
        mongo_collection: The collection to insert the document into
        **kwargs: The key-value pairs for the new document
    Returns:
        The _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
