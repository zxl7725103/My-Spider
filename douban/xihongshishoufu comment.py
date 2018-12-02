import requests
import json
import time
import random

def get_page(html):   #获取页面内容
    headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'
    }
    response=requests.get(html,headers=headers)
    if response.status_code==200:
        print(response.text)
        return response.text
    return None

def parse_page(html):   #解析页面内容
    data=json.loads(html)['cmts']   #页面内容是json格式，以json格式读取
    for item in data:
        yield {                              #该方法返回一个字典，以每一评论为元素的字典类型
            'comment':item['content'],
            'time':item['time'].split(' ')[0],
            'city':item['cityName'],
            'nickname':item['nickName'],
            'rate':item['score']
        }



def save_to_text():
   for i in range(1,10):
       url='http://m.maoyan.com/mmdb/comments/movie/1212592.json?_v_=yes&offset='+str(i)
       html=get_page(url)
       print('正在保存第%d页'% i)
       for item in parse_page(html):
           with open('西红柿首富.txt','a',encoding='utf-8') as f:
               f.write(item['time']+','+item['nickname']+','+item['city']+','+str(item['rate'])+','+item['comment']+'\n')
       time.sleep(3+float(random.randint(1,100))/20)   #设置随机数反爬


def repeat_del(old,new):    #去重
    oldfile=open(old,'r',encoding='utf-8')
    newfile=open(new,'w',encoding='utf-8')
    content_list=oldfile.readlines() #按行读取数据
    newcontent=[]   #新的评论存储为一个列表。
    for line in content_list:
        if line not in newcontent:
            newfile.write(line)  #将不重复的写进文本文件中
            newcontent.append(line)   #将不重复的写进列表
def intwenben(name):    #文本初始化，创建文本，删除文本内的内容。
    with open(name,'w') as f:
        f.truncate()






if __name__=='__main__':
    intwenben('西红柿首富.txt')
    intwenben('西红柿首富new.txt')
    save_to_text()
    repeat_del('西红柿首富.txt','西红柿首富new.txt')