import re
import requests
from bs4 import  BeautifulSoup

#把键值对与数字对应生成字典
def numbers():
    f=open("F:\Python\My Spider to Github\dazhongdianpin\zifu.txt",'r')
    number='960219038469776553021457'
    num_list=list(number)
    #print(len(num_list))
    f=f.read()
    f=f.split('.')
    d={}
    for n in f:
        if "uta" in n:     #数字的class特征，是以uta开头的。
            #print(n)
            nu=n.split(':')
            nu=nu[1].strip('-')
            w=n.split('{')   #获取明文
            #print(w[0])
            try:   #对无法匹配的进行pass。
             for i in range(24):  #一一对应进行匹配，和偏移量一致的就是对应的密码
                e=8+14*i
                if int(nu)==e:
                    d['<d class="{0}"></d>'.format(w[0])]=num_list[i]   #构造整体的替换字典
                    next(i)
            except:
                pass
    print(d)
    return d
#把键值对替换为对应的字符
def change(dic,text):
    for key,value in dic.items():
        text=text.replace(key,value)
    return text

def Getbasic_messege(url):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'cy=8; cye=chengdu; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=167d63acb41c8-0c43a499a834ca-b781636-144000-167d63acb42c8; _lxsdk=167d63acb41c8-0c43a499a834ca-b781636-144000-167d63acb42c8; _hc.v=fd88fdf3-b87e-1c1e-4ec7-40a6e55f7749.1545487437; s_ViewType=10; _lxsdk_s=167d6e22995-8a0-399-06d%7C%7C0',
        'Host': 'www.dianping.com',
        'Referer':"http://www.dianping.com/shop/93195650",
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    }
    response=requests.get(url,headers=headers)
    #print(response.text)
    soup=BeautifulSoup(response.text,'lxml')

    tel_soup=re.findall(r'</span>(.*?)</p>',change(dt,str(soup.find('p',class_='expand-info tel'))))[0]
    #加上[0]，可以提起里面里面的字符串。提取电话的明文，进行整体替换后，就为电话号码的明文
    print(tel_soup)

dt=numbers()
url='http://www.dianping.com/shop/93195650'
basic_messegae=Getbasic_messege(url)


