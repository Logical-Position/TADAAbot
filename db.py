import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import jsonify

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
    pass

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
    pass

def delete():
    pass
