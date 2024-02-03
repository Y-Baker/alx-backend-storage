#!/usr/bin/env python3

"""Task 102"""

from pymongo import MongoClient

if __name__ == "__main__":
    """print log stats from nginx logs in MongoDB"""

    client = MongoClient('localhost', 27017)
    nginx = client.logs.nginx

    print("{} logs".format(nginx.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(method,
                                       nginx.count_documents({
                                           "method": method
                                           })))
    print(f'{nginx.count_documents({
        "method": "GET",
        "path": "/status"
        })} status check')
    print("IPs:")

    results = nginx.aggregate([
        {"$group": {
            "_id": "$ip",
            "total": {"$sum": 1}
        }},
        {"$sort": {
            "total": -1
        }},
        {"$limit": 10}
    ])
    for one in results:
        print(f"\t{one.get('_id')}: {one.get('total')}")
