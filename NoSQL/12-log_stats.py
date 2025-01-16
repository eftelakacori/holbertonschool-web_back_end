#!/usr/bin/env python3 
"""A Python script that provides some stats
about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    # Connect to MongoDB client
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the logs.nginx collection
    nginx_collection = client.logs.nginx
    
    # Count and print the total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Initialize a dictionary to count each HTTP method
    methods_count = {"GET": 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}
    
    # Count the number of occurrences for each HTTP method
    for method in methods_count:
        methods_count[method] = nginx_collection.count_documents({"method": method})

    # Print the method statistics
    print("Methods:")
    for method, count in methods_count.items():
        print(f"\tmethod {method}: {count}")

    # Count the number of GET requests with path '/status'
    status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")
