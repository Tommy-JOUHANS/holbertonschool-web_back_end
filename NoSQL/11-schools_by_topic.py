#!/usr/bin/env python3
"""Python function that returns a list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools having a specific topic
    Args:
        mongo_collection: The collection to query
        topic: The topic to search for
    Returns:
        A list of schools having the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
