import os
import requests
import json

def find_class_info():

    cookies = {
        '_ga': 'GA1.2.1179830460.1510250977',
        '__utma': '117564634.1179830460.1510250977.1511049538.1512078967.2',
        '__utmz': '117564634.1512078967.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    }

    headers = {
        'Origin': 'https://cab.brown.edu',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://cab.brown.edu/',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    params = (
        ('output', 'json'),
        ('page', 'asoc.rjs'),
        ('route', 'course'),
    )

    data = [
      ('term', '201720'),
      ('course', 'CSCI%201550'),
      ('id', '25756'),
      ('instId', ''),
    ]

    res = requests.post('https://cab.brown.edu/asoc-api/', headers=headers, params=params, cookies=cookies, data=data)
    print("content: ")
    print(res.content)
    print(res.status_code)
    parsed = res.json()
    print("attempting to interpret parsing: ")
    #print typeof(parsed)
    print(parsed["sections"][0]["avail"])
    return res.json()

def post_course(dept, code, crn):

    dept = dept.upper()
    encoded = "%20".join([dept, code])

    cookies = {
        '_ga': 'GA1.2.1179830460.1510250977',
        '__utma': '117564634.1179830460.1510250977.1511049538.1512078967.2',
        '__utmz': '117564634.1512078967.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    }

    headers = {
        'Origin': 'https://cab.brown.edu',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://cab.brown.edu/',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    params = (
        ('output', 'json'),
        ('page', 'asoc.rjs'),
        ('route', 'course'),
    )

    data = [
      ('term', '201720'),
      # needs to parse spaces to remove %20
      #('course', 'CSCI%201550'),
      ('course', encoded),
      #('id', '25756'),
      ('id', crn),
      ('instId', ''),
    ]

    res = requests.post('https://cab.brown.edu/asoc-api/', headers=headers, params=params, cookies=cookies, data=data)
    print("content: ")
    print(res.content)
    print("status code: " + str(res.status_code))
    return res

def parse_JSON(res):
    """
    Returns a dict containing JSON information for the class
    """
    parsed = res.json()
    print("parsed: ")
    print(parsed)
    return parsed["sections"][0]

