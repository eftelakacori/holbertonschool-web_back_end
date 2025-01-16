#!/usr/bin/env python3 
"""A Python script that provides some stats
about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

# Connect to the MongoDB client
client = MongoClient('localhost', 27017)

# Access the 'logs' database and the 'nginx' collection
db = client.logs
collection = db.nginx

# Get the total number of logs
total_logs = collection.count_documents({})

# Get the count of documents for each HTTP method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

# Get the number of GET requests with path "/status"
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

# Display the results
print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check_count} status check")
