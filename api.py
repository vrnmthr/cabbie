import requests


def get_srcdb(year, semester):
    """
    :returns srcdb param given a year and a semester
    """
    sem_vals = {
        'fall': '10',
        'spring': '20',
        'summer': '00',
        'winter': '15',
    }
    srcdb = str(year - 1) + sem_vals[semester]
    return srcdb


def raw_query(query, year, semester, is_alias=True):
    """
    Searches for a query, does not include independent study classes.
    Year must be a valid year.
    If is_alias=True, assumes that the query is a course code. Otherwise, does a keyword search.
    Returns dict with response.
    """
    url = "https://cab.brown.edu/api/"

    search_type = 'alias' if is_alias else 'keyword'

    querystring = {"page": "fose", "route": "search", search_type: query, "is_ind_study": "N"}

    headers = {
        'accept': "application/json, text/javascript, */*; q=0.01",
        'origin': "https://cab.brown.edu",
        'x-requested-with': "XMLHttpRequest",
        'content-type': "application/json",
        'cache-control': "no-cache",
    }

    srcdb = get_srcdb(year, semester)
    data = {
        "other": {"srcdb": srcdb},
        "criteria": [
            {"field": search_type, "value": query},
            {"field": "is_ind_study", "value": "N"}
        ]
    }

    response = requests.request("POST", url, json=data, headers=headers, params=querystring)
    return response.json()
