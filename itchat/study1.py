import itchat

itchat.auto_login(hotReload=True)
#加上hotReload==True,那么就会保留登录的状态，至少在后面的几次登录过程中不会再次扫描二维码，该参数生成一个静态文件itchat.pkl用于存储登录状态
#itchat.send('test ok','filehelper')
seng_userid="晓亮"   #设置微信好友昵称
itchat_user_name=itchat.search_friends(name=seng_userid)[0]['UserName']
#查找微信好友的微信识别码
itchat.send_msg('这是一个测试',itchat_user_name)
#向微信好友发送信息
print(itchat_user_name)
#打印好友的微信识别码。

