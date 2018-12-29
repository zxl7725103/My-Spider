import re
import requests
from bs4 import  BeautifulSoup


def change(dic,text):
    for key,value in dic.items():
        text=text.replace(key,value)
    return text

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
    #print(d)
    return d


def Get_chinese():  #汉字密文获取
    text=[]
    url='http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/e0bc4731b17d81a0d3ecee18b2b0c52d.svg'
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    for i in soup.select('textpath'):
       text.append(i.text)  #解析处出密文后，放入text列表中
    path={}
    for i in soup.select('path'):   #解析文字位置。
        d=re.findall(r'M0 (.*?) H600',i['d'])[0]
        d=str(int(d)-23)
        path[d]=i['id']
    #print(path)

    return text,path   #返回密文和密文的位置


def chinese(text,path):
    c = open("F:\Python\My Spider to Github\dazhongdianpin\chinese.txt", 'r') #读取字符编码CSS文件信息
    #print(c.read())
    c=c.read()
    w=c.split(';}.')   #第一次以";}."拆分
    w[0]=w[0].strip('.')  #对第一个去除符号"."
    #print(len(w))
    ch={}
    n=0
    for i in range(len(w)-1):
            i=w[i]
            n=n+1
            f=i.split('{')   #第二次以"{"拆分
            #print(i)
            k=str(f[0])     #拆分后分为2个元素，一个为[0],一个为[1]
            row=re.findall(r'background:-(.*?).0px -',f[1])[0]   #分别查找字符的纵坐标和和横坐标
            col=re.findall(r'px -(.*?).0px',f[1])[0]
            #print(text)
            try:
               if "nz" in k:   #在字符串中查找含有"nz"的字符串，
                #print(k)
                 c_col=int(int(path[col])-1)   #转换为int类型
                 c_row=int((int(row)/14))
                #print(c_col,c_row)
                 c_list=list(text[c_col])
                #print(m)
                 ch['<b class="{0}"></b>'.format(k)]=c_list[c_row]  #构造汉字的查找字典
            except:
                pass
    return ch

def Get_comments(ch,url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'cy=8; cye=chengdu; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=167d63acb41c8-0c43a499a834ca-b781636-144000-167d63acb42c8; _lxsdk=167d63acb41c8-0c43a499a834ca-b781636-144000-167d63acb42c8; _hc.v=fd88fdf3-b87e-1c1e-4ec7-40a6e55f7749.1545487437; s_ViewType=10; _lxsdk_s=167d6e22995-8a0-399-06d%7C%7C0',
        'Host': 'www.dianping.com',
        'Referer': "http://www.dianping.com/shop/93195650",
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    }
    response = requests.get(url, headers=headers)
    # print(response.text)
    soups = BeautifulSoup(response.text, 'lxml')
    soup=soups.find_all('li',class_="comment-item")
    for i in soup:
        s=str(i.find('p',class_='desc'))
        e=change(ch,s)  #替换字符串中的字符为汉字
        comment=re.findall('class="desc">(.*?)</p>',e)[0]
        print(comment.replace('<br/><br/>',""))  #replace 去除掉字符串中的"br"换行符


#把键值对替换为对应的字符

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
    basic_messegae={}
    basic_messegae['tel']=re.findall(r'</span>(.*?)</p>',change(dt,str(soup.find('p',class_='expand-info tel'))))[0]
    #加上[0]，可以提起里面里面的字符串。提取电话的明文，进行整体替换后，就为电话号码的明文
    basic_messegae['comments_num']=re.findall(r'> (.*?) 条评论',change(dt,str(soup.find('span',id="reviewCount"))))[0]
    e=change(dt,str(soup.find('span',id="avgPriceTitle")))
    basic_messegae['人均:']=re.findall(r'>人均: (.*?)</span>',e)[0]
    print(basic_messegae)

#dt=numbers()  #dt是数字字典
text,path=Get_chinese()
ch=chinese(text,path)
url='http://www.dianping.com/shop/58137369'
#basic_messegae=Getbasic_messege(url)
basic_comments=Get_comments(ch,url)


