import requests
import json
import itchat

KEY='309b48cf4c214d938d90fb4ab0562872'  #apikey
apiurl='http://openapi.tuling123.com/openapi/api/v2'  #api网址

def response(msg):
    data = {
        "perception": {
            "inputText": {
                "text": msg
            },
        },
        "userInfo": {
            "apiKey": KEY,
            'userId': 'test'
        }
    }
    # 发送的数据格式
    dat = json.dumps(data)  # 将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
    try:

        r = requests.post(apiurl, data=dat).json()
        print(r)
        return r['results'][0]['values']['text']
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultreply='I Recived: '+ msg['Text'] +'现在有点忙,请稍等' #如果机器人出故障的回复。
    reply=response(msg['Text'])
    return reply or defaultreply
itchat.auto_login(hotReload=True)
itchat.run()
