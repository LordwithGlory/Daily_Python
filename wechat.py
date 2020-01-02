import re
import time
import itchat
from itchat.content import *

# python装饰器
@itchat.msg_register([TEXT])
def text_reply(msg):
    # msg['FromUserName']是加密之后的微信昵称 ，通过这个来获得好友信息表
    friend = itchat.search_friends(userName=msg['FromUserName'])
    replyContent = "收到您在 %s 发送的【%s】"% (time.strftime('%m-%d %H:%M',time.localtime()),msg['Type'])
    if msg['Type'] == 'Text':
        if re.search(r"快乐",msg['Content']):
            replyContent+="吃好喝好长生不老[耶][耶][耶]"
            itchat.send('@img@%s' % 'https://pic1.zhimg.com/50/v2-343589c34d4ed45b70fe6667f5f959db_hd.jpg',
                        toUserName=msg['FromUser'])
    # friend里面的参数Nickname和remarkname，tousername是指的用户ID
    # msg['Text']是消息内容
    itchat.send("好友【%s (昵称：%s)】于：【%s】发来消息：【%s】"% (friend['NickName'], friend['RemarkName'],
                time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),msg['Text']),toUserName='filehelper')
    itchat.send(replyContent,toUserName=msg['FromUserName'])
    # msg['Content']也是消息内容
    print("时间为[%s] 收到好友[%s 昵称: %s] 发来的 【%s】:[%s]" % (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),
            friend['NickName'],friend['RemarkName'],msg['Type'],msg['Content']))
# 免得重新登陆            
itchat.auto_login(hotReload=True)
itchat.run()