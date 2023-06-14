from sqlite_manager import SqliteManager
from requests import request

# db_name = 'test.db'
DB_NAME = 'test_full-schema.db'
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
        'table': 'auditData',
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

db = SqliteManager(DB_NAME, DB_SCHEMA)

# API - Connecting
# Not sure exactly what's needed here
def open_connection():
    pass

def close_connection(exception):
    if (exception):
        print(exception)
    db.disconnect()

# API - Creating Data
def create_audit(clientName, domain, data):
    res = db.create_audit()
    return jsonify(res), 200

# API - Reading Data
def get_all_clients():
    res = db.query('select * from clients')
    return {"clients": res}

def get_data_for_audit(auditId):
    pass

def get_all_audits_for_client(clientId):
    pass

def get_most_recent_audit_for_client(clientId):
    pass

# API - Updating Data

# Would an audit ever be updated? 
#   I think a new audit would be created, or the old one would just be deleted
#   I can't think of a scenario where the data would need to be edited afterwards

# API - Deleting Data
def delete_audit(auditId):
    pass

def delete_client(clientId):
    pass



# Starter CRUD Functions
# -- Deprecated --

def create():
    return {"create": "not implemented"}

def read():
    return get_all_clients()

def update():
    return {"update": "not implemented"}

def delete():
    return {"delete": "not implemented"}
