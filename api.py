# TODO Get data objects from these APIs:
#  Moz,
#  AHREFS,
#  SEMRUSH,
#  Search Console,
#  Siteliner,
#  Copyscape,
#  Google Mobile Friendliness,

import requests
import


def get_moz_data_obj():
    moz_endpoint = 'https://lsapi.seomoz.com/v2/'
    auth = ('mozscape-99d452d879', 'ddd3ecda33aaf804302522fd557b2c5')

    links_endpoint = moz_endpoint + 'links'
    data = """{
            "target": "moz.com/blog",
            "target_scope": "page",
            "filter": "external+nofollow",
            "limit": 5
        }"""

    r = requests.get('https://lsapi.seomoz.com/v2/links', data=data, auth=auth)
    print(r)



