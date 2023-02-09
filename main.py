from flask import Flask, jsonify, render_template, request, send_file
import os
import tadaa
import time


UPLOAD_DIR = '/path/to/uploads'

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
def do_something():
    # Parse form and get exports filepath
    # Generate audit
    inputID = 'spreadsheet-selection'
    for file in request.files.getlist(inputID):
        print(file.name)
        print(file.stream)
        print(file.filename)
    # TODO: get local filepaths
    # TODO: call TADAA to generate report
    # TODO: enable "Download report" button once audit finishes running
    data = tadaa.test_run()
    print(data)
    time.sleep(3)
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/download', methods=['GET'])
def download_audit():
    ppt_path = tadaa.test_run()
    return send_file(ppt_path)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
