from sqlite_manager import SqliteManager
from flask import jsonify
from requests import request

dbName = 'test.db'
# dbSchema = [
#     {
#         'name': 'clients',
#         'columns': [
#             'id',
#             'name',
#         ],
#     },
#     {
#         name: 'audits',
#         columns: [
#             'id',
#             'clientId',
#             'domain',
#             'timestamp',
#             'projectType',
#         ],
#     },
#     {
#         name: 'auditData',
#         columns: [
#             'auditId',
#             'clientId',
#             # The following is copy-pasted from data_fields of utils.py
#             # TODO: Find a way to re-use the array
#             'broken__4xx_or_5xx',
#             'broken_internal_urls',
#             'broken_external_urls',
#             'h1__tag_is_empty',
#             'urls_with_duplicate_h1',
#             'external_redirected_urls',
#             'missing_alt_text',
#             'internal_redirected_urls',
#             'description_is_empty',
#             'description_is_missing',
#             'description_length_too_long',
#             'description_length_too_short',
#             'not_found_by_the_crawler',
#             'duplicate_meta_descriptions',
#             'title_tag_length_too_long',
#             'title_tag_length_too_short',
#             'duplicate_page_titles',
#             'url_in_multiple_xml_sitemaps',
#             'noindex_url_in_xml_sitemaps',
#             'redirect__3xx__url_in_xml_sitemaps',
#         ],
#     },
# ]

db = SqliteManager(dbName, None)

# API - Creating Data
def create_audit(clientName, domain, data):
    res = db.create_audit()
    return jsonify(res), 200

# API - Reading Data
def get_all_clients():
    pass

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
    res = db.create()
    return jsonify(res), 200

def read():
    res = db.read()
    return jsonify(res), 200

def update():
    res = db.update()
    return jsonify(res), 200

def delete():
    res = db.delete()
    return jsonify(res), 200
