import requests
from urllib.parse import urlencode #导入urlencode 模块

def get_page(offset):
    params={
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    url='https://www.toutiao.com/api/search/content/?'+urlencode(params)
   # print(url)
    try：
        response=requests.get(url)
        if response==200:
            return response.json()
    except requests.ConnectionError :
        return None

def get_image=(json):
    if json.get('data'):
        for item in json.get('data')
            title=item.get('title')
            image=item.get('image_url')

get_page(20)
