#!/usr/bin/env python3
"""A Python script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    # Lidhja me MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')  # Përdorni 127.0.0.1 ose localhost për ndërlidhjen lokale
    db = client.logs  # Baza e të dhënave logs
    nginx_collection = db.nginx  # Koleksioni nginx në bazën e të dhënave logs
    
    # Llogarit numrin total të dokumenteve në koleksionin nginx
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Llogarit numrin e dokumenteve për secilën metodë HTTP
    methods_count = {"GET": 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}
    for method in methods_count:
        methods_count[method] = nginx_collection.count_documents({"method": method})
    
    print("Methods:")
    for method, count in methods_count.items():
        print(f"\tmethod {method}: {count}")
    
    # Llogarit numrin e dokumenteve për metodën GET dhe path = "/status"
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
