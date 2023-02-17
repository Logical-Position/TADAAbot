from flask import Flask, jsonify, render_template, request, send_file
from werkzeug.utils import secure_filename

import os
import tadaa
import time


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
    for file in request.files.getlist(inputID):
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_DIR'], filename))

    tadaabject = tadaa.parse_data(UPLOAD_DIR)

    root_path = app.root_path
    pop_ppt = tadaa.generate_audit(tadaabject, root_path)

    time.sleep(3)
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route('/download', methods=['GET'])
def download_audit():
    ppt_path = app.root_path + '/populated_ppt.pptx'
    return send_file(ppt_path)
    #return 'Send file'  # send_file(ppt_path)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
