# -*- coding '':''  utf-8 -*-''
# @Time      '':''  2020/5/4  22:34''
# @author    '':''  zxl7725103''
# @Software  '':''  PyCharm''
# @CSDN      '':''  https://me.csdn.net/qq_45906219''
# @knowlege :enumerate函数进行遍历、文件夹的创建和去重、Yeild 返回数组方式、
#            global headers全局变量、
#            python 多进程的调用、re模块的学习





import requests
from urllib.parse import urlencode  # 构造url
import time
import os
from hashlib import md5
from lxml import etree
from bs4 import BeautifulSoup
import re
from multiprocessing.pool import Pool
import json

def get_pages(offset):

    global headers #请求头需要重复使用

    headers = {
        'authority': 'www.toutiao.com',
        'accept': 'application/json, text/javascript',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.toutiao.com/search/?keyword=%E7%BE%8E%E5%A5%B3',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '__tasessionId=ytsejkbfg1588565377624; csrftoken=c18330764ea241ab3038217f43f4727d; tt_webid=6822836390284871176; s_v_web_id=k9ryt6g8_GdQsF5UM_2VB6_4GKc_Ayp8_5rTzFvms3Wav; ttcid=36eba985c88e4ee096bae3de9323eacc31',
    }

    params = (
        ('aid', '24'),
        ('app_name', 'web_search'),
        ('offset', offset),
        ('format', 'json'),
        ('keyword', '\u7F8E\u5973'),
        ('autoload', 'true'),
        ('count', '20'),
        ('en_qc', '1'),
        ('cur_tab', '1'),
        ('from', 'search_tab'),
        ('pd', 'synthesis'),
        ('timestamp', '1588565417157'),
        ('_signature', 'QrHPiAAgEBBqO4NBQxHtnUKwjpAABwg'),
    )

    response = requests.get('https://www.toutiao.com/api/search/content/', headers=headers, params=params)
    response.content.decode('utf-8')
    #print(response.text)
    if response.status_code==200:

          return response.json()
def get_images(jsons):
    if jsons['data']:
       #print('ok')
       #print(json['data'])
       for item in jsons['data']:
           if item.get('title') is None:
               continue
           title=item.get('title')

           print(title)
           if item.get('source_url')==None:
               continue
           article_url=item.get('source_url')
           article_url='https://www.toutiao.com'+article_url
           rr=requests.get(article_url,headers=headers)
           if rr.status_code==200:
                #print(rr.text)
                pat = ' content:(.*?).slice'
                match = re.search (pat, rr.text, re.S) #re.search会在给定字符串中寻找第一个匹配给定正则表达式的子字符串
                if match != None:
                    image_urls=re.findall(r'img src&#x3D;\\&quot;(.*?)\\&quot;',match.group(), re.S)
                    #image_urls=image_urls.encode('utf-8').decode('unicode_escape')
                    print(image_urls)
                    yield {         # 返回标题和网址
                        'title':title,
                        'images':image_urls
                    }
                    continue
                rrs = re.findall(r'JSON.parse\(\"(.*?)\"\)', rr.text)
                print(rrs)
                if rrs != None:
                    liantu_image_urls=[]
                    r = rrs[0].encode('utf-8').decode('unicode_escape')
                    r = r.replace ('\\', '')

                    print(r)
                    q = json.loads(r)
                    for item in q['sub_images']:
                        image_urls=item['url']
                        liantu_image_urls.append(image_urls)
                    yield {  # 返回标题和网址
                            'title': title,
                            'images': liantu_image_urls
                    }


def save_images(content):
    path='F://Python//今日头条图片//今日头条美女//'   # 保存目录
    if not os.path.exists(path):             #创建目录
        os.mkdir(path)
        os.chdir (path)
    else:
        os.chdir(path)

    if not os.path.exists(content['title']):
        title = content['title']
        os.mkdir (title + '//')  # 创建文件夹
        os.chdir (title + '//')
        print (title)
    else:
        title = content['title']
        os.chdir (title + '//')
        print (title)

    for q,u in enumerate(content['images']):  #enumerate函数进行遍历 q表示序列值，u 表示 值
        u = u.encode ('utf-8').decode ('unicode_escape')
        print(u)
        # 先编码在解码 获得需要的网址链接
        #  开始下载
        r = requests.get (u, headers=headers)
        if r.status_code == 200:
            # file_path = r'{0}/{1}.{2}'.format('美女', q, 'jpg')  # 文件的名字和地址，用三目运算符来调试文件夹的名字
            # hexdisgest() 返回十六进制图片
            with open (str (q) + '.jpg', 'wb') as fw:
                fw.write (r.content)
                print (f'该系列----->下载{q}张')

def main(offset):
    jsons = get_pages(offset)
    #print(json)

    get_images(jsons)
    print(get_images(jsons))
    for content in get_images(jsons):
        try:
            print(content)
            save_images(content)
        except FileExistsError and OSError:
            print('创建文件格式错误，包含特殊字符串:')
            continue


if __name__ == '__main__':
    pool = Pool()
    groups = [j * 20 for j in range(2)]
    #main(groups)
    print(groups)
    pool.map(main, groups) # 传offset偏移量
    pool.close()
    pool.join()