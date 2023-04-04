from flask import Flask, jsonify, render_template, request, redirect, send_file, url_for
# from flask_dance.contrib.google import make_google_blueprint, google

import os
import tadaa
import time
import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')

app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR

# Google OAuth dance setup
# app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
# app.config["GOOGLE_OAUTH_CLIENT_ID"] = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
# app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
# # We think the scopes provided are the cause of LACK OF PERMISSIONS error
# # TODO: Determine if these strings are defined by Google or Flask Dance
# # TODO: Discover needed scopes
# # google_bp = make_google_blueprint(scope=["profile", "email"])
# app.register_blueprint(google_bp, url_prefix="/login")

cred = credentials.Certificate('path/to/keys')
fs_app = firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/main')
def get_main():
    return render_template('main.html')

@app.route('/results')
def get_results():
    return render_template('results.html')

@app.route('/auth')
def auth_dance():
    if not google.authorized:
        return redirect(url_for("google.login"))
    userRes = google.get("/oauth2/v1/userinfo")
    print("You are {email} on Google".format(email=userRes.json()["email"]))
    # print(resp.json())
    # assert resp.ok, resp.text
    # return "You are {email} on Google".format(email=resp.json()["email"])
    #resp = google.get("/webmasters/v3/sites")
    # assert resp.ok, resp.text
    return userRes.json()

@app.route('/extras')
def get_extras():
    return render_template('extras.html')

@app.route('/faq')
def get_faq():
    return render_template('faq.html')

@app.route('/', methods=['POST'])
def parse_upload():
    inputID = 'spreadsheet-selection'

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    project_dir = os.path.join(app.config['UPLOAD_DIR'], timestamp)

    os.makedirs(project_dir, exist_ok=True)
    files = [file for file in request.files.getlist(inputID) if file.filename]
    for file in files:
        filename = os.path.basename(file.filename)
        file.save(os.path.join(project_dir, filename))

    proj_files = os.listdir(project_dir)
    segments = proj_files[0].split('_')
    project_name = segments[0].split('.')[0]

    tadaabject = tadaa.parse_data(project_dir)

    root_path = app.root_path
    pop_ppt = tadaa.generate_audit(tadaabject, project_dir, root_path, project_name)

    time.sleep(1.5)
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route('/download', methods=['GET'])
def download_audit():
    dirs = os.listdir(UPLOAD_DIR)
    last_dir = dirs[-1]
    abs_path_proj_dir = app.root_path + '/uploads/' + last_dir
    files = os.listdir(abs_path_proj_dir)
    segments = files[0].split('_')
    project_name = segments[0].split('.')[0]
    ppt_path = os.path.join(UPLOAD_DIR, abs_path_proj_dir + f'/{project_name}.pptx')

    return send_file(ppt_path)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
