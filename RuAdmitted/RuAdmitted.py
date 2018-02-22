# -*- coding: utf-8 -*-
#!/usr/bin/python

import urllib, urllib2, cookielib
from BeautifulSoup import BeautifulSoup
import time, os

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def post():
    global result
    url = "https://admissionservices.rutgers.edu/graduate/programStatus.app"

    payload = {
                "ssn" : xxxx,
                "dobMonth" : "xxx",
                "dobDay" : xx,
                "dobYear" : xxxx,
                "genderCode" : "x",
                "submitBtn" : "Submit"
               }
    data = urllib.urlencode(payload)

    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    res = opener.open(url)
    cookies = ""
    for item in cookie:
        cookies = cookies + item.name + "=" + item.value + ";"

    headers = {
                "Host": "admissionservices.rutgers.edu",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                "Referer": "https://admissionservices.rutgers.edu/graduate/programStatusLogon.app",
                "Cookie": cookies,
                "Connection": "close",
                "Upgrade-Insecure-Requests": "1",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "79"
              }

    req = urllib2.Request(url, data, headers)
    page = urllib2.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html)
    result = soup.findAll('table')[2].findAll('tr')[1].findAll('td')[5].text.strip()

    print result

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((
        Header(name, 'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def send():
    from_addr = 'xxxxx@sina.com'
    password = 'xxxxx'
    to_addr = 'xxxx@qq.com'
    smtp_server = 'smtp.sina.com'

    msg = MIMEText(result, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'一个奇妙的脚本 <%s>' % from_addr)
    msg['To'] = _format_addr(u'汤包包 <%s>' % to_addr)
    msg['Subject'] = Header(u'RU录取结果查询', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

def main():
    post()
    send()

if __name__ == "__main__":
    while (1):
        try:
            main()
            time.sleep(3600)
        except:
            pass
