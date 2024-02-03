#!/usr/bin/env python3
"""Task 8"""


def list_all(mongo_collection):
    """lists all documents in a collection"""

    return list(mongo_collection.find())
