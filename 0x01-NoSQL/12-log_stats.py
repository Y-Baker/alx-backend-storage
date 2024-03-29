#!/usr/bin/env python3

"""Task 12"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    nginx = client.logs.nginx

    print("{} logs".format(nginx.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(method, nginx.count_documents({"method": method})))
    print(f'{nginx.count_documents({"method": "GET", "path": "/status"})} status check')
