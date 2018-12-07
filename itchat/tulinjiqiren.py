import requests
import json

KEY='309b48cf4c214d938d90fb4ab0562872'  #apikey
apiurl='http://openapi.tuling123.com/openapi/api/v2'  #api网址
data={
    "perception": {
        "inputText": {
            "text": "附近的酒店名称"
        },
    },
    "userInfo":{
        "apiKey":KEY,
        'userId': 'test'
    }
}
#发送的数据格式
dat=json.dumps(data) #将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
r=requests.post(apiurl,data=dat).json()
print(r)
