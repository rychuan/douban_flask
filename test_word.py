# -*- codeing = utf-8 -*-
# @Time     : 11/17 12:06
# @Author   : River
# @File     : test_word.py
# @Software : PyCharm


from flask import Flask, render_template
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3
import jieba

con = sqlite3.connect('movie.db')
cur = con.cursor()

sql = "select instroduction from movie250"
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
cur.close()
con.close()

cut = jieba.cut(text)
string = ' '.join(cut)
img = Image.open(r'.\static\assets\img\tree.jpg')
img_array = np.array(img)
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc"
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off') #是否显示坐标轴

# plt.show()
plt.savefig(r'.\static\assets\img\word.jpg', dpi=500)