# TODO Get data objects from these APIs:
#  Moz,
#  AHREFS - will need to upgrade from our legacy plan to a new plan
#  SEMRUSH,
#  Search Console, - Google data will come from Google Project Dashboard, where APIs are accessed
#  Siteliner,
#  Copyscape,
#  Google Mobile Friendliness,
#  Pagespeed Insights,

# Cache/cookie? previously saved api creds until they don't work again, then prompt when needed?
# What questions do we want to ask of the data?
# Google Data Studio/Looker?

import argparse
import httplib2
import requests

from collections import defaultdict
from dateutil import relativedelta
from googleapiclient.discovery import build
from oauth2client import client
from oauth2client import file
from oauth2client import tools
from creds import *


creds = sc_json


def authorize_creds(creds, authorizedcreds='authorizedcreds.dat'):
    """
    Authorize Search Console credentials using OAuth2.
    @param [str] creds: the path to the client_secrets.json file
    @param [str] authorizedcreds: file name for a .dat file used for caching credentials.
    @return [obj] webmasters_service: a Resource to interact with the API using the Authorized HTTP Client.
    """
    print('Authorizing SC Creds')
    # Variable parameter that controls the set of resources that the access token permits.
    SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

    # Path to client_secrets.json file
    CLIENT_SECRETS_PATH = creds

    # Create a parser to be able to open browser for Authorization
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[tools.argparser])
    flags = parser.parse_args([])

    # Creates an authorization flow from a clientsecrets file.
    # Will raise InvalidClientSecretsError for unknown types of Flows.
    flow = client.flow_from_clientsecrets(
        CLIENT_SECRETS_PATH, scope=SCOPES,
        message=tools.message_if_missing(CLIENT_SECRETS_PATH))

    # Prepare credentials and authorize HTTP
    # If they exist, get them from the storage object
    # credentials will get written back to the 'authorizedcreds.dat' file.
    storage = file.Storage(authorizedcreds)
    credentials = storage.get()

    # If authenticated credentials don't exist, open Browser to authenticate
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(flow, storage, flags)  # Add the valid creds to a variable

    # Take the credentials and authorize them using httplib2
    http = httplib2.Http()  # Creates an HTTP client object to make the http request
    http = credentials.authorize(http=http)  # Sign each request from the HTTP client with the OAuth 2.0 access token
    webmasters_service = build('searchconsole', 'v1',
                               http=http)  # Construct a Resource to interact with the API using the Authorized HTTP Client.

    print('SC Auth Successful')
    return webmasters_service


# API for testing structured data?
# url = 'https://api.microlink.io'
# params = {'url': 'https://www.deepcoat.com/', 'meta': 'True'}
#
# response = requests.get(url, params)
#
# print(response.json())
