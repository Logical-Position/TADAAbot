from flask import Flask, g, jsonify, render_template, request, redirect, send_file, url_for
import re
import datetime
import json
import os
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
data_labels = {}


# TADAA Routes

@app.route('/', methods=['GET', 'POST'])
def index():
    with open('ppts/json/original.json') as t:
        ppt_schema = json.load(t)
        # tmplname = ppt_schema['ppt']
        slides = ppt_schema['slides']

    # for slide in slides:
    #     if 'inputs' in slide:
    #         for input in slide['inputs']:
    #             data_labels.append(input['id'])

    if request.method == 'GET':
        page_title = "TADAAbot"
        return render_template('index.html', page_title=page_title, slides=slides)
    elif request.method == 'POST':
        # 1. Gather uploaded data: files and fields
        # 2. Call tadaa to parse and compile data
        # 3. Send compiled data to:
        #       - Frontend
        #       - Database

        # Get data from form
        for label in manual_data_labels:
            data = request.form.get(label, '')
            manual_data[label] = data
        print("")
        print(" ===== D A T A ===== ")
        print(manual_data)
        print("\n\n")
        # Create folder for audit assets
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        project_dir = os.path.join(app.config['UPLOAD_DIR'], timestamp)

        # Save uploaded files
        inputID = 'spreadsheet-selection'
        os.makedirs(project_dir, exist_ok=True)
        files = [file for file in request.files.getlist(inputID) if file.filename]
        for file in files:
            filename = os.path.basename(file.filename)
            file.save(os.path.join(project_dir, filename))

        # Create project name
        # Get project name from front-end and sanitize
        def sanitize_input(input_str):
        # Regular expression to blocklist script tags
            sanitized_str = re.sub(r'<script\b[^>]*>(.*?)</script>', '', input_str, flags=re.IGNORECASE)
            return sanitized_str
        
        project_name = sanitize_input(request.form.get("domain_url"))

        # Let TADAA do it's thing
        root_path = app.root_path
        data = tadaa.__generate_audit(project_dir, manual_data, root_path, project_name, timestamp, ppt_schema)

    # And also return it to the client
    return jsonify(data)

@app.route('/gen-ppt', methods=['POST'])
def generate_ppt():
    # 1. Collect form data
    # 1.5 Handle file uploads: https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/
    # 2. Let TADAA do it's thing
    # 3. And also return it to the client
    # data = tadaa.generate_ppt()
    # return jsonify(data)
    return jsonify({})

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
