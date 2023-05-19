from flask import Flask, jsonify, render_template, request, redirect, send_file, url_for

from flask_dance.contrib.google import make_google_blueprint, google

import os
import tadaa
import time
import datetime
import db_controller as db


app = Flask(__name__)

# For user-uploaded Excel files
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_DIR'] = UPLOAD_DIR

# Google OAuth dance setup
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
app.config["GOOGLE_OAUTH_CLIENT_ID"] = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
# We think the scopes provided are the cause of LACK OF PERMISSIONS error
# TODO: Determine if these strings are defined by Google or Flask Dance
# TODO: Discover needed scopes
google_bp = make_google_blueprint(scope=["profile", "email"])
app.register_blueprint(google_bp, url_prefix="/login")


# TADAA Routes

# TODO: Combine these '/' routes
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def parse_upload():
    inputID = 'spreadsheet-selection'

    print(request.form['domain_url'])

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


# API Routes

@app.route('/auth')
def auth_dance():
    if not google.authorized:
        return redirect(url_for("google.login"))
    userRes = google.get("/oauth2/v1/userinfo")
    siteList = google.get("/webmasters/v3/sites")
    print(siteList.json())
    print("You are {email} on Google".format(email=userRes.json()["email"]))
    return siteList.json()
    # return "You are {email} on Google".format(email=userRes.json()["email"])


# Database Routes

@app.route('/test/create', methods=['GET', 'POST'])
def db_createData():
    if request.method == 'POST':
        print("POST request")
        return db.create()
    elif request.method == 'GET':
        print("GET request")
        return db.create()
    else:
        return "Some other request"

@app.route('/test/read', methods=['GET'])
def db_readData():
    return db.read()

@app.route('/test/update', methods=['POST', 'PUT'])
def db_updateData():
    return db.update()

@app.route('/test/delete', methods=['GET', 'DELETE'])
def db_deleteData():
    return db.delete()


# Main Function

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))