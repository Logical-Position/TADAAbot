from flask import Flask, jsonify, render_template, request, redirect, send_file, url_for

# Flask Dance
from flask_dance.contrib.google import make_google_blueprint, google

# Google API
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import os
import tadaa
import time
import datetime
import db_controller as db
import json


app = Flask(__name__)

# For user-uploaded Excel files
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_DIR'] = UPLOAD_DIR

# Google OAuth dance setup
# app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")

# app.config["GOOGLE_OAUTH_CLIENT_ID"] = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
# app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
# # We think the scopes provided are the cause of LACK OF PERMISSIONS error
# # TODO: Determine if these strings are defined by Google or Flask Dance
# # TODO: Discover needed scopes
# google_bp = make_google_blueprint(scope=["profile", "email"])
# app.register_blueprint(google_bp, url_prefix="/login")



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

    # An example of getting "Manual Input Data" from form
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
def api_test():
    # Define the auth scopes to request.
    scope = 'https://www.googleapis.com/auth/analytics.readonly'
    key_file_location = 'key.json'

    # Authenticate and construct service.
    analytics_service = get_service(
            api_name='analytics',
            api_version='v3',
            scopes=[scope],
            key_file_location=key_file_location)

    accounts = get_accounts(analytics_service)
    return accounts
    #profile_id = get_first_profile_id(analytics_service)
    #print_results(get_results(analytics_service, profile_id))

    #print(service)
    #return {"success": "true"}
    
    # if not google.authorized:
    #     return redirect(url_for("google.login"))
    # userRes = google.get("/oauth2/v1/userinfo")
    # siteList = google.get("/webmasters/v3/sites")
    # print(siteList.json())
    # print("You are {email} on Google".format(email=userRes.json()["email"]))
    # return siteList.json()
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





# API Functions

def get_service(api_name, api_version, scopes, key_file_location):
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        key_file_location: The path to a valid service account JSON key file.

    Returns:
        A service that is connected to the specified API.
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)

    return service

def get_accounts(service):
    # Get a list of all Google Analytics accounts for this user
    accounts = service.management().accounts().list().execute()
    print(accounts)
    return accounts

def get_first_profile_id(service):
    # Use the Analytics service object to get the first profile id.

    # Get a list of all Google Analytics accounts for this user
    accounts = service.management().accounts().list().execute()

    if accounts.get('items'):
        # Get the first Google Analytics account.
        account = accounts.get('items')[0].get('id')

        # Get a list of all the properties for the first account.
        properties = service.management().webproperties().list(
                accountId=account).execute()

        if properties.get('items'):
            # Get the first property id.
            property = properties.get('items')[0].get('id')

            # Get a list of all views (profiles) for the first property.
            profiles = service.management().profiles().list(
                    accountId=account,
                    webPropertyId=property).execute()

            if profiles.get('items'):
                # return the first view (profile) id.
                return profiles.get('items')[0].get('id')

    return None

def get_results(service, profile_id):
    # Use the Analytics Service Object to query the Core Reporting API
    # for the number of sessions within the past seven days.
    return service.data().ga().get(
            ids='ga:' + profile_id,
            start_date='7daysAgo',
            end_date='today',
            metrics='ga:sessions').execute()

def print_results(results):
    # Print data nicely for the user.
    if results:
        print('View (Profile):', results.get('profileInfo').get('profileName'))
        print('Total Sessions:', results.get('rows')[0][0])

    else:
        print('No results found')


# Main Function

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))