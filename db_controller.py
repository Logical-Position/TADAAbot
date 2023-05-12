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

