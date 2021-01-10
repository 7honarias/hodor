#!/usr/bin/python3
import requests

url = 'http://158.69.76.135/level0.php'
response = requests.get(url)
text = response.text.split()
try:
    txtId = text.index(str(2224))
except:
    txtId = 0
currentVote = 0
if (text[txtId+3]).isdigit():
    currentVote = int(text[txtId+3])

print("current vote are {}".format(currentVote))
for x in range(currentVote, 1025):
    sender = requests.post(url, {'id': 2224, 'holdthedoor': 'submit'})
    if sender.status_code is 200 and "Holdor" in sender:
        currentVote += 1
        print("ok vote # {}".format(currentVote), end="\r", flush=True)
    else:
        print("fail one vote")
print("Total: {} exit program success".format(currentVote))
