import itchat
from itchat.content import *


#@itchat.msg_register(TEXT)  #不带具体对象注册, 将注册为普通消息的回复方法。
#def simple_reply(msg):
    #print(msg['Text'])
    #itchat.send_msg('已经收到消息，内容为：%s'%msg['Text'],msg['FromUserName'])
    #return "I recived: %s"%msg['Text']

@itchat.msg_register(TEXT,isFriendChat=True,isGroupChat=True,isMpChat=True)
#带对象参数注册, 对应消息对象将调用该方法，其中isFriendChat表示好友之间，isGroupChat表示群聊，isMapChat表示公众号。
def reply(msg):
    msg.user.send(("%s:%s") % (msg.type,msg.text))
itchat.auto_login(hotReload=True)
itchat.run()