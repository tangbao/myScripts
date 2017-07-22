# -*- coding: utf-8 -*-
#!/usr/bin/python
import requests

URL = "http://app.greentree.cn/Api/index.php/User/registration"

print "your userId:"
userId = raw_input()
print "your deviceId:"
deviceId = raw_input()
print "your osversion:"
osversion = raw_input()

payload = {
            "userId" : userId
           }

headers = {
            "weblogid": "",
            "deviceId": deviceId,
            "sourceId": "Channel07",
            "session": "1",
            "versionCode": "1",
            "carrier": "",
            "screensize": "1080x1920",
            "protocolVer": "1.2.0",
            "platform": "Android",
            "osversion": osversion,
            "macAddress": "",
            "subSourceId": "Channel07",
            "model": "",
            "clientVer": "4.2.0",
            "Content-Length": "23",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "app.greentree.cn",
            "Connection": "Keep-Alive"
          }

r = requests.post(URL, data=payload, headers=headers)
print r.text
