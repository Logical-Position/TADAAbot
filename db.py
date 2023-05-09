import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import jsonify
from requests import request


# Use a service account.
cred = credentials.Certificate('key.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()
ref = db.collection('test')

def connect():
    pass

def disconnect():
    pass

def create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json['test']
        ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

def read():
    try:
        # Check if ID was passed to URL query
        # todo_id = request.args.get('id')
        # if todo_id:
        #     todo = ref.document(todo_id).get()
        #     return jsonify(todo.to_dict()), 200
        # else:
        all_todos = [doc.to_dict() for doc in ref.stream()]
        return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

def update():
    """
        update() : Update document in Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    try:
        id = request.json['id']
        ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"
    
def delete():
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        ref.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"
