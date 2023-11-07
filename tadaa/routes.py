from flask import jsonify, render_template, request, redirect, send_from_directory, url_for, Response, abort
from flask_login import login_required, login_user, logout_user, current_user
import json
import os
from uuid import uuid4
from werkzeug.utils import secure_filename

from tadaa import app
from tadaa import auth
from tadaa import tadaa


def get_schema(name:str='schema'):
    schema_path = os.path.join(app.config['DATA_DIR'], 'json', f"{name}.json")
    with open(schema_path) as f:
        schema = json.load(f)
    return schema

def is_allowed_filetype(filename:str):
    # FIXME: I think this is currently excluding folders
    #return '.' in filename and \
    #    filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_FILES']
    return True

def save_files(filelist:list, path:str=''):
    for file in filelist:
        base_filename = os.path.basename(file.filename)
        if base_filename != '' and is_allowed_filetype(base_filename):
            os.makedirs(path, exist_ok=True)
            filename = secure_filename(base_filename)
            file.save(os.path.join(path, filename))

# Routes
@app.route('/', methods=['GET'])
@login_required
def index():
    schema = get_schema()
    return render_template('views/index.html', schema=schema)

@app.route('/generate-presentation', methods=['POST'])
@login_required
def generate_presentation():
    schema = get_schema()
    
    form_data = request.form.to_dict()
    
    audit_id = f"{form_data['domain_url']}-{str(uuid4())}"
    data_dir = os.path.join(app.config['AUDITS_DIR'], audit_id)

    sitebulb_files = request.files.getlist('spreadsheet-selection')
    save_files(sitebulb_files, data_dir)
    
    serp_images = request.files.getlist('')
    save_files(serp_images, data_dir)

    semrush_images = request.files.getlist('')
    save_files(semrush_images, data_dir)

    domauth_images = request.files.getlist('dom_auth_screenshot-image')
    save_files(domauth_images, data_dir)

    sitebulb_csvs = [os.path.join(data_dir, os.path.basename(file.filename)) for file in sitebulb_files if file.filename != '']
    audit_data = tadaa.run_audit(sitebulb_csvs)
    
    template_path = os.path.join(app.config['DATA_DIR'], 'pptx', schema['ppt'])
    output_path = os.path.join(data_dir, audit_id)
    tadaa.create_presentation(template_path, output_path, audit_data)

    tadaabject = {
        'id': audit_id,
        'data': audit_data
    }

    return jsonify(tadaabject)

# NOTE: If requesting to redownload a previous powerpoint, browser caches previous download and looks to pull from cache first.
@app.route('/download/<id>', methods=['GET'])
@login_required
def download_presentation(id):
    presentation_path = os.path.join(app.config['AUDITS_DIR'], id)
    filename = f"{id}.pptx"
    return send_from_directory(presentation_path, filename, as_attachment=True)


# Authentication

# somewhere to login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # If the user is already authenticated, redirect them to the index page
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == auth.USERNAME and password == auth.PASSWORD:
            login_user(auth.lp_user, remember=True)
            return redirect(url_for('index'))

        # If no matching user is found, return a 401 Unauthorized response
        print("User not found or invalid credentials.")
        return abort(401)

    print("Get or login failed.")
    return render_template('views/login.html')

# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

# Error Handling
# 401 unauthorized
@app.errorhandler(401)
def page_not_found(e):
    return redirect(url_for('login'))