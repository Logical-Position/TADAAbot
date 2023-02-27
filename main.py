from flask import Flask, jsonify, render_template, request, send_file
from flask_dance.contrib.google import make_google_blueprint, google


import os
import tadaa
import time
import datetime


UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')

app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/main')
def get_main():
    return render_template('main.html')

@app.route('/results')
def get_results():
    return render_template('results.html')


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

    time.sleep(3)
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
