# -*- coding: utf-8 -*-
import urllib2
import urllib
import os

os.environ["http_proxy"] = '127.0.0.1:8080'

def brute_force(user, password):

    # proxy = urllib2.ProxyHandler({"http":'http://127.0.0.1:8080'})
    # opener = urllib2.build_opener(proxy)
    # urllib2.install_opener(opener)

    url = "http://demo.testfire.net/bank/login.aspx"
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    headers = {"User-Agent":user_agent,"Content-Type": "application/x-www-form-urlencoded", "Referer": "http://demo.testfire.net/bank/login.aspx"}
    values = {'uid': user, 'passw': password,'btnSubmit':'Login'}
    data = urllib.urlencode(values)
    request = urllib2.Request(url,data,headers)
    response = urllib2.urlopen(request)
    #print response.code

brute_force(user="admin",password="123456")