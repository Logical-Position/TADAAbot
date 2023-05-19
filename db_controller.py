from sqlite_manager import SqliteManager
from flask import jsonify
from requests import request

db = SqliteManager("test.db")

def create():
    res = db.create()
    return jsonify(res), 200

def read():
    res = db.read()
    return jsonify(res), 200

def update():
    res = db.update()
    return jsonify(res), 200

def delete():
    res = db.delete()
    return jsonify(res), 200



# API - Creating Data
def create_audit(clientName, domain, data):
    pass

# API - Reading Data
def get_all_clients():
    pass

def get_data_for_audit(auditId):
    pass

def get_all_audits_for_client(clientId):
    pass

def get_most_recent_audit_for_client(clientId):
    pass

# API - Updating Data

# Would an audit ever be updated? 
#   I think a new audit would be created, or the old one would just be deleted
#   I can't think of a scenario where the data would need to be edited afterwards

# API - Deleting Data
def delete_audit(auditId):
    pass

def delete_client(clientId):
    pass