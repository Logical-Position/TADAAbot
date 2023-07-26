from flask import Flask, g, jsonify, render_template, request, redirect, send_file, url_for

# Flask Dance
from flask_dance.contrib.google import make_google_blueprint, google

# Google API
# from apiclient.discovery import build
# from oauth2client.service_account import ServiceAccountCredentials

import os
import time
import sqlite3
from uuid import uuid4

# import db_controller as db
import tadaa
import datetime
# import db_controller as db
import json


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
    # 1. Gather uploaded data: files and fields
    # 2. Call tadaa to parse and compile data
    # 3. Send compiled data to:
    #       - Frontend
    #       - Database

    # Get data from form
    for label in manual_data_labels:
        data = request.form.get(label, '')
        manual_data[label] = data
    
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
    proj_files = os.listdir(project_dir)
    segments = proj_files[0].split('_')
    print("segments:", segments)

    # Get project name from front-end and sanitize
    project_name = request.form.get("project-name")
    # project_name = segments[0].split('.')[0]
    print("Project name:", project_name)

    # Let TADAA do it's thing
    # TODO: Refactor tadaa to return the final tadaabject in one line
    tadaabject = tadaa.parse_data(project_dir, manual_data)
    root_path = app.root_path
    pop_ppt = tadaa.generate_audit(tadaabject, project_dir, root_path, project_name)

    # Save tadaabject to database
    # TODO: Refactor this into tadaa
    audits_id = str(uuid4())
    client_id = str(uuid4())
    domain = manual_data["domain_url"]
    project_type = "InvalidType"

    # TODO: Refactor this into the final tadaabject
    data = {
        "audits_id": audits_id,
        "client_id": client_id,
        "client_name": project_name,
        "domain": domain,
        "ts": timestamp,
        "project_type": project_type,
        "ppt_url": pop_ppt,
    }
    db_init(DB_SCHEMA)
    db_insert_new_audit(data)

    # And also return it to the client
    return jsonify(data)

@app.route('/download/<ts>', methods=['GET'])
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
    project_name = files[0]
    ppt_path = os.path.join(UPLOAD_DIR, abs_path_proj_dir + f'/{project_name}')
    # print(ppt_path)
    return send_file(ppt_path)




























# EVERYTHING DATABASE.
# wHY ARE THEY SO SIMPLE IN THEORY, BUT IMPLEMENTING THEM IS
# SUCH. A. BITCH.

DB_NAME = 'db'
DB_FILENAME = f'{DB_NAME}_partial-schema.db'
DB_ROUTE = f'/{DB_NAME}'

# Schema
#
# clients
#   id: UUID
#   name: string
#
# audits
#   id: UUID
#   client_id: UUID
#   domain: string
#   timestamp: Timestamp
#   projectType: ProjectType
#   pptUrl: URL
#
# audit_data
#   TODO
#
DB_SCHEMA = [
    {
        'table': 'clients',
        'columns': [
            'id',
            'name',
        ],
    },
    {
        'table': 'audits',
        'columns': [
            'id',
            'clientId',
            'domain',
            'timestamp',
            'projectType',
            'pptUrl'
        ],
    },
    {
        'table': 'audit_data',
        'columns': [
            'auditId',
            'clientId',
            # The following is copy-pasted from data_fields of utils.py
            # TODO: Find a way to re-use the array
            'broken__4xx_or_5xx',
            'broken_internal_urls',
            'broken_external_urls',
            'h1__tag_is_empty',
            'urls_with_duplicate_h1',
            'external_redirected_urls',
            'missing_alt_text',
            'internal_redirected_urls',
            'description_is_empty',
            'description_is_missing',
            'description_length_too_long',
            'description_length_too_short',
            'not_found_by_the_crawler',
            'duplicate_meta_descriptions',
            'title_tag_length_too_long',
            'title_tag_length_too_short',
            'duplicate_page_titles',
            'url_in_multiple_xml_sitemaps',
            'noindex_url_in_xml_sitemaps',
            'redirect__3xx__url_in_xml_sitemaps',
        ],
    },
]

def db_connect():
    """
    Creates a connection to the database.
    @return A database connection.
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_FILENAME)
    return db


def db_disconnect():
    """
    Properly disconnects from database.
    This function should be called at app close.
    @return None
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def db_init(schema):
    """
    Initializes the database with the given schema.
    @param schema: The schema with which to structure the database.
    @return None
    """
    db = db_connect()
    cur = db.cursor()
    for table in schema:
        table_name = table['table']
        if not db_table_exists(table_name):
            cols = table['columns']
            db_create_table(table_name, cols)


def db_create_table(name, cols):
    """
    Creates a table with the given name and columns.
    @param [str] name: The name of the table to create.
    @param [array] cols: An array of string.
    @return None
    """
    db = db_connect()
    cur = db.cursor()
    # It is not advised to interpolate strings in a query like this, 
    # https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries
    #   but it's the only option. See the Stack Overflow link below.
    # At least it's not from user input, it's a variable defined directly above.
    # Should still (probably) be sanitized if it's going to be used in this way.
    # (I suppose this is encouragement to move initialization to a .sql file)
    # https://stackoverflow.com/questions/4308124/safe-way-to-create-sqlite3-table-in-python
    q = f"CREATE TABLE IF NOT EXISTS {name}("
    initial = True
    for col in cols:
        if initial:
            q += f"{col}"
            initial = False
        else:
            q += f", {col}"
    q += f")"
    cur.execute(q)
    db.commit()
    cur.close()


"""
Checks if the given table exists in the database.
@param [str] name: The name of the table to verify.
@return [bool] : True if the table exists, otherwise False
"""
def db_table_exists(name):
    db = db_connect()
    cur = db.cursor()
    query = f"SELECT name FROM sqlite_master WHERE type='table' and name='{name}'"
    cur.execute(query)
    res = cur.fetchall()
    count = len(res)
    exists = True if count == 1 else False
    cur.close()
    return exists

def db_id_exists_in_table(val, table_name):
    db = db_connect()
    cur = db.cursor()
    q = f"SELECT * FROM {table_name} WHERE id = '{val}'"
    cur.execute(q)
    res = cur.fetchall()
    count = len(res)
    exists = True if count == 1 else False
    cur.close()
    return exists

def db_client_exists(val):
    return db_id_exists_in_table(val, "clients")

def db_audit_exists(val):
    return db_id_exists_in_table(val, "audits")

def db_insert_into(table_name, data):
    # TODO: Check if data length is equal to num cols for table
    db = db_connect()
    cur = db.cursor()

    q = f"INSERT INTO {table_name} VALUES ("
    initial = True
    for datum in data:
        if initial:
            q += "?"
            initial = False
        else:
            q += ", ?"
    q += ")"
    cur.execute(q, data)
    db.commit()
    cur.close()

def db_insert_new_audit(data):
    # data = {
    #     "client_name": project_name,
    #     "domain": manual_data["domain_url"],
    #     "ts": timestamp,
    #     "project_type": project_type,
    #     "ppt_url": pop_ppt,
    # }

    # Pull data from input
    audits_id = data['audits_id']
    client_id = data['client_id']
    client_name = data['client_name']
    domain = data['domain']
    ts = data['ts']
    project_type = data['project_type']
    ppt_url = data['ppt_url']

    # Form data for database submission

    # clients
    #   id: UUID
    #   name: string
    client_data = [
        client_id,
        client_name
    ]

    # audits
    #   id: UUID
    #   client_id: UUID
    #   domain: string
    #   timestamp: Timestamp
    #   projectType: ProjectType
    #   pptUrl: URL
    audits_data = [
        audits_id,
        client_id,
        domain,
        ts,
        project_type,
        ppt_url,
    ]

    # Insert into database
    db_insert_into("clients", client_data)
    db_insert_into("audits", audits_data)


def db_query(query, args=(), one=False):
    cur = db_connect().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def db_read_all():
    all_data = {}
    for table in DB_SCHEMA:
        table_name = table['table']
        q = f"SELECT * FROM {table_name}"
        a = []
        all_data[table_name] = db_query(q, a)
    return all_data

def db_read_table(table_name):
    if db_table_exists(table_name):
        q = f"SELECT * FROM {table_name}"
        a = []
        data = db_query(q, a)
    return data

def db_read_id_from_table(id, table_name):
    db = db_connect()
    cur = db.cursor()
    q = f"SELECT * FROM {table_name} WHERE id = '{id}'"
    cur.execute(q)
    res = cur.fetchone()
    return res

def db_read_audit(ts):
    q = f""
    a = []
    data = db_query(q, a)
    return data

def db_delete_all():
    db = db_connect()
    cur = db.cursor()
    for table in DB_SCHEMA:
        table_name = table['table']
        q = f"DELETE FROM {table_name}"
        cur.execute(q)
    db.commit()
    
# Database Testing Routes

@app.route(f'{DB_ROUTE}/all', methods=['GET'])
def db_route_read_all():
    db_init(DB_SCHEMA)
    data = db_read_all()
    return jsonify(data)

@app.route(f'{DB_ROUTE}/<val>', methods=['GET'])
def db_route_read_data(val):
    db_init(DB_SCHEMA)
    if db_table_exists(val):
        # Fetch table data
        data = { "table": db_read_table(val) }
    elif db_client_exists(val):
        data = { "client": db_read_id_from_table(val, "clients") }
    elif db_audit_exists(val):
        data = { "audit": db_read_id_from_table(val, "audits") }
    else:
        data = {"error": f"{val} does not exist as a table, or client ID, or audit ID"}
    return jsonify(data)


@app.teardown_appcontext
def close_connection(exception):
    db_disconnect()
































# Main Function

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))