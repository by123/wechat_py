import itchat, time
from itchat.content import *

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('很高兴认识你!')


itchat.auto_login(hotReload=True)
itchat.run(True)
