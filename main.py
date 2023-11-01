from flask import Flask, g, jsonify, render_template, request, redirect, send_file, url_for
import re
import datetime
import json
import os
import tadaa

app = Flask(__name__)

# For user-uploaded Excel files
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
ROOT_PATH = app.root_path
app.config['UPLOAD_DIR'] = UPLOAD_DIR

schema = None
with open('ppts/json/schema.json') as t:
    schema = json.load(t)

# Routes
@app.route('/', methods=['GET'])
def index():
    page_title = "TADAA"
    return render_template('index.html', page_title=page_title, schema=schema)

@app.route('/gen-ppt', methods=['POST'])
def generate_ppt():
    form_data = request.form.to_dict()

    # Handle file uploads: https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/ <-- idk how to apply this
    export_files = [file for file in request.files.getlist('spreadsheet-selection') if file.filename]

    tadaabject = tadaa.generate_ppt(form_data, export_files, schema)

    return jsonify(tadaabject)

@app.route('/download/<ts>', methods=['GET'])
# If requesting to redownload a previous powerpoint, browser caches previous download and pull from cache instead of server if cache is present.
def download_audit(ts):
    dirs = os.listdir(UPLOAD_DIR)
    # FIXME: This has not been getting the correct ppts
    # FIXED: but leaving temporarily for discussion purposes.
    # Per the documentation, os.listdir returns a list,
    #   but "The list is in arbitrary order"
    # https://docs.python.org/3/library/os.html?highlight=listdir#os.listdir
    # last_dir = dirs[-1]
    # print(dirs)
    # print(last_dir)

    # TODO: This can likely be simplified by just getting the full download path from the client
    requested_audit = ts
    abs_path_proj_dir = app.root_path + '/uploads/' + requested_audit
    files = os.listdir(abs_path_proj_dir)
    project_name = ''
    for file in files:
        if file.endswith('.pptx'):
            project_name = file

    project_name_split = project_name.split(".")
    #final_project_name = project_name_split[0]

    # Name differs when first sending out file vs when pulling from URL query.
    # This probably won't be an issue moving forward if we request downloads using ID's or via other methods.
    ppt_path = os.path.join(UPLOAD_DIR, abs_path_proj_dir + f'/{project_name}')

    #return send_file(ppt_path, mimetype=None, as_attachment=True, attachment_filename=(final_project_name + "-" + requested_audit + ".pptx"))
    return send_file(ppt_path)
#NEW DEF
def get_ppt(id):
    # path = get_ppt_for(id)
    return send_file("/path/to/ppt")

# Main Function
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
