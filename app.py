from flask import Flask
import os

app = Flask(__name__)

# For user-uploaded Excel files
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
ROOT_PATH = app.root_path
app.config['UPLOAD_DIR'] = UPLOAD_DIR