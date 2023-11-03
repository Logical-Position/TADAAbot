from flask import jsonify, render_template, request, send_file, send_from_directory
import json
import os
from uuid import uuid4
from werkzeug.utils import secure_filename

from tadaa import app
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
def index():
    schema = get_schema()
    return render_template('views/index.html', schema=schema)

@app.route('/generate-presentation', methods=['POST'])
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
def download_presentation(id):
    presentation_path = os.path.join(app.config['AUDITS_DIR'], id)
    filename = f"{id}.pptx"
    return send_from_directory(presentation_path, filename, as_attachment=True)