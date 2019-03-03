import requests
import json
import time
import pymongo
import numpy as np
# mongodb数据库初始化
client = pymongo.MongoClient('localhost', 27017)
# 指定数据库
db = client.ITjuzi
# 指定集合，类似于mysql中的表
mongo_collection1 = db.itjuzi_investevent

def save_to_mongo(response):
    data=json.loads(response)
    try:
        for i in range(0,20):
            #时间戳转换
            timestamp = int(data['data']['data'][i]['time'])  # 获取时间戳
            # 转换成localtime
            time_local = time.localtime(timestamp)
            # 转换成新的时间格式(2016-05-05 20:28:54)
            dt = time.strftime("%Y-%m-%d", time_local)  #获取时间
            company=data['data']['data'][i]['name']   #获取公司名称
            com_scope=data['data']['data'][i]['com_scope']   #获取公司名称
            rounds=data['data']['data'][i]['round']   #获取轮次
            money = data['data']['data'][i]['money']  # 获取金额
            print(dt,company,com_scope,rounds,money)
            mongo_collection1.insert_one({'时间':dt,'公司名称':company,'所属行业':com_scope,'轮次':rounds,'金额':money})
    except Exception as e:
           print(e)




def page_content(url,pages):
    cookies = {
        'acw_tc': '76b20f4815515132072791271ed5d61515e37f6943cf09a36737c92f66417b',
        'gr_user_id': '2363e0a3-9aae-4680-bf16-6b3e69d1006f',
        'gr_session_id_eee5a46c52000d401f969f4535bdaa78': 'f8c248f5-51bf-4537-b513-b12042bb52ae',
        'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1551513208,1551599653',
        'gr_session_id_eee5a46c52000d401f969f4535bdaa78_f8c248f5-51bf-4537-b513-b12042bb52ae': 'true',
        'flag': '699624--18980065548',
        '_ga': 'GA1.2.1457456770.1551599656',
        '_gid': 'GA1.2.1926198936.1551599656',
        '_gat_gtag_UA_59006131_1': '1',
        'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1551600087',
    }

    headers = {
        'Origin': 'https://www.itjuzi.com',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'CURLOPT_FOLLOWLOCATION': 'true',
        'Authorization': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5pdGp1emkuY29tL2FwaS9hdXRob3JpemF0aW9ucyIsImlhdCI6MTU1MTYwMDA3OCwiZXhwIjoxNTUxNjg2NDc4LCJuYmYiOjE1NTE2MDAwNzgsImp0aSI6IlNjVExsNWlvSDB1NzQ3bzciLCJzdWIiOjY5OTYyNCwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.CEpr8IPA4rvg0qLeClzFLJBt2-82nkSt4nRJ6PPQr4M',
        # 'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.itjuzi.com/investevent',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Connection': 'keep-alive',
    }
    url = "https://www.itjuzi.com/api/investevents"
    data = {"pagetotal": 0, "total": 0, "per_page": 20, "page": pages, "type": 1, "scope": "", "sub_scope": "", "round": [],
            "valuation": [], "valuations": "", "ipo_platform": "", "equity_ratio": [""], "status": "", "prov": "",
            "city": [], "time": [], "selected": "", "location": "", "currency": [], "keyword": ""}
    response = requests.post(url, data=data, headers=headers, cookies=cookies)
    return response.text


if __name__=='__main__':
    pages=2
    url='https://www.itjuzi.com/investevent'
    page=0
    while page<pages:
        page_s=page_content(url,page+1)
        page=page+1
        print(page_s)
        save_to_mongo(page_s)