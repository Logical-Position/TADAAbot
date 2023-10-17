# TODO Get data objects from these APIs:
#  Moz,
#  AHREFS - will need to upgrade from our legacy plan to a new plan
#  SEMRUSH,
#  Search Console, - Google data will come from Google Project Dashboard, where APIs are accessed
#  Siteliner,
#  Copyscape,
#  Google Mobile Friendliness,
#  Pagespeed Insights,




# ------------- Search Console--------------------




# -----------------COPYSCAPE----------------------

def copyscape(username, key):
    copyscape_url = f'https://www.copyscape.com/api/?u={username}&k={key}&o=csearch&x=1&f=json'
    copyscape_response = requests.get(copyscape_url).json()
    copyscape_results_list = copyscape_response['result']
    copyscape_num_result_urls = copyscape_response['count']

    print(copyscape_results_list)

# ------------------Structured/Meta Data from Microlink----------------------


def microlink(target_url):  # https://api.microlink.io
    params = {'url': f'{target_url}', 'meta': 'True'}
    response = requests.get(target_url, params)
    print(response.json())


# ------------------SEMRUSH-----------------------------

def semrush(username, key):  # Need to upgrade account
    pass


# -------------------AHREFS----------------------------

def ahrefs(username, key):  # Need to upgrade account
    pass


# -------------------MOZ----------------------------

def moz(username, key):
    pass