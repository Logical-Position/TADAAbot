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

# TODO: Code the options and labels here instead.
#   Keys should be used as IDs.
# tadaaptions = ta_decisions.json 

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
    # FIXME: Refactor this value
    inputID = 'spreadsheet-selection'

    # Get data from form
    for label in manual_data_labels:
        data = request.form.get(label, '')
        manual_data[label] = data
    
    print(manual_data)

    # Create folder for assets
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    project_dir = os.path.join(app.config['UPLOAD_DIR'], timestamp)

    # Save uploaded files
    os.makedirs(project_dir, exist_ok=True)
    files = [file for file in request.files.getlist(inputID) if file.filename]
    for file in files:
        filename = os.path.basename(file.filename)
        file.save(os.path.join(project_dir, filename))

    # Create project name
    proj_files = os.listdir(project_dir)
    segments = proj_files[0].split('_')
    project_name = segments[0].split('.')[0]

    # TADAA does it's thing
    tadaabject = tadaa.parse_data(project_dir, manual_data)
    root_path = app.root_path
    pop_ppt = tadaa.generate_audit(tadaabject, project_dir, root_path, project_name)

    # Have to return something...
    # TODO: Find out how to use this value on the frontend
    # TODO: Replace it with the tadaabject and use this to populate a 'Results' view
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
    print(ppt_path)
    return send_file(ppt_path)


# Database Routes

db_root = '/test'

@app.route(f'{db_root}/create', methods=['GET', 'POST'])
def db_createData():
    return db.create_audit('example.com', 'Example', {'data': 'something'})

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