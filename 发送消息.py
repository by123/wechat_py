import itchat

itchat.auto_login(hotReload=True)

#发送文本消息
itchat.send('Hello, by', toUserName='@2d16a9753bdf5642c9ede2820b3f021e7f20538214a049d6781113005854bb8a')

#发送图片
itchat.send_image("imgs/image1.jpg",'@2d16a9753bdf5642c9ede2820b3f021e7f20538214a049d6781113005854bb8a')

#发送视频
itchat.send_video("video.mp4",'@2d16a9753bdf5642c9ede2820b3f021e7f20538214a049d6781113005854bb8a')

#发送音频
itchat.send_file("audio.mp3",'@2d16a9753bdf5642c9ede2820b3f021e7f20538214a049d6781113005854bb8a')

