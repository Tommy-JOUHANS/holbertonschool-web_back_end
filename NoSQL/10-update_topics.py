#!/usr/bin/env python3
"""Python function that changes all topics of a school
document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name
    Args:
        mongo_collection: The collection to update the document in
        name: The name of the school to update
        topics: The list of topics to set for the school
    Returns:
        The number of documents updated
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": {'$each': topics}}})
    return result.modified_count
