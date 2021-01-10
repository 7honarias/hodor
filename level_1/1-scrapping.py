#!/usr/bin/python3
"""Hodor 1
   Use: ./1.py
   The program obtain #votes current and just sending the necessary votes.
"""
import requests
from requests.exceptions import TooManyRedirects

ID = 2224
url = 'http://158.69.76.135/level1.php'
response = requests.get(url)
text = response.text.split()
key = response.cookies['HoldTheDoor']
cookie = {'HoldTheDoor': key}
try:
    txtId = text.index(str(ID))
except:
    txtId = 0
currentVotes = 0
if (text[txtId+3]).isdigit():
    currentVotes = int(text[txtId+3])
print("current votes is {}".format(currentVotes))

for x in range(currentVotes, 4096):
    sender = requests.post(url, {'id': ID, 'holdthedoor': 'submit', 'key': key}, cookies=cookie)
    if sender.status_code is 200 and 'Hold' in sender.text:
        print("vote ok", end='\r', flush=True)
    else:
        print("fail vote")

print("end program")