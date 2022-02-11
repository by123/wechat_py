import itchat
import math
import os

#给auto_login方法传入值为真的hotReload.即使程序关闭，一定时间内重新开启也可以不用重新扫码
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]

import re
siglist = []
for i in friends:
    nickName = i["NickName"].strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1f\d+\w*|[<>/=]")
    nickName = rep.sub("", nickName)
    siglist.append(nickName)

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import jieba
import numpy as np
from PIL import Image


# 读入背景图片
abel_mask = np.array(Image.open('imgs/bg.jpg'))

# 读取要生成词云的文件
wordlist = jieba.cut(siglist, cut_all=True)
word_space_split = "".join(siglist)
#word_space_split = "".join(wordlist)
#print(wordlist)
print("---------------------------------------------")
#print(word_space_split)

# my_wordcloud = WordCloud().generate(word_space_split) 默认构造函数
my_wordcloud = WordCloud(
                         background_color='black',  # 设置背景颜色
                         mask=abel_mask,  # 设置背景图片
                         max_words=622,  # 设置最大显示的个数
                         stopwords=STOPWORDS,  # 设置停用词
                         font_path='heiti.ttf',  # 设置字体格式，如不设置显示不了中文
                         max_font_size=50,  # 设置字体最大值
                         random_state=42,  # 设置有多少种随机生成状态，即有多少种配色方案
                         scale=10
                         ).generate(word_space_split)

# 根据图片生成词云颜色
image_colors = ImageColorGenerator(abel_mask)
# my_wordcloud.recolor(color_func=image_colors)

# 以下代码显示图片
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()


