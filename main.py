from flask import Flask, jsonify, render_template, request, redirect, send_file, url_for

import datetime
import json
import os
import time
import db_controller as db
import tadaa

app = Flask(__name__)

# For user-uploaded Excel files
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_DIR'] = UPLOAD_DIR


manual_data_labels = [
    'domain_url',
    'cms',
    'sc_access',
    'ga_access',
    'mobility_issues',
    'sitemap_submitted',
    'sitemap_url',
    'robots_url',
    'structured_data',
    'site_content_ux',
    'dupe_content',
    'calls_to_action',
    'blog',
    'canonicals',
    'web_security',
    'desktop_speed',
    'broken_backlinks',
]

manual_data = {}

# TADAA Routes

# TODO: Combine these '/' routes
@app.route('/', methods=['GET'])
def index(): 
    # Accessing manual input options in json file
    with open('ta_decisions.json') as t:
        ta_decisions = json.load(t)

    return render_template('index.html', ta_decisions=ta_decisions)

@app.route('/', methods=['POST'])
def parse_upload():
    print("U P L O A D   P O S T")
    # FIXME: Refactor this value
    inputID = 'spreadsheet-selection'

    for label in manual_data_labels:
        data = request.form.get(label, '')
        manual_data[label] = data
    
    print(manual_data)

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

    print(project_name)

    # TODO: parse_data needs to do something with manual_data
    tadaabject = tadaa.parse_data(project_dir, manual_data)

    root_path = app.root_path
    pop_ppt = tadaa.generate_audit(tadaabject, project_dir, root_path, project_name)

    print("")

    time.sleep(1.5)
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/download', methods=['GET'])
def download_audit():
    print("D O W N L O A D   R O U T E")
    dirs = os.listdir(UPLOAD_DIR)
    # FIXME: This has not been getting the correct ppts
    # Per the documentation, os.listdir returns a list,
    #   but "The list is in arbitrary order"
    # https://docs.python.org/3/library/os.html?highlight=listdir#os.listdir
    last_dir = dirs[-1]
    print(dirs)
    print(last_dir)
    abs_path_proj_dir = app.root_path + '/uploads/' + last_dir
    files = os.listdir(abs_path_proj_dir)
    segments = files[0].split('_')
    project_name = segments[0].split('.')[0]
    print(project_name)
    ppt_path = os.path.join(UPLOAD_DIR, abs_path_proj_dir + f'/{project_name}.pptx')
    print(ppt_path)
    print("")
    return send_file(ppt_path)


# Database Routes

db_root = '/test'

@app.route(f'{db_root}/create', methods=['GET', 'POST'])
def db_createData():
    if request.method == 'POST':
        print("POST request")
        return db.create()
    elif request.method == 'GET':
        print("GET request")
        return db.create()
    else:
        return "Some other request"

@app.route(f'{db_root}/read', methods=['GET'])
def db_readData():
    return db.read()

@app.route(f'{db_root}/update', methods=['POST', 'PUT'])
def db_updateData():
    return db.update()

@app.route(f'{db_root}/delete', methods=['GET', 'DELETE'])
def db_deleteData():
    return db.delete()


# Main Function

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))