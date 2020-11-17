from flask import Flask, render_template
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3
import jieba


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    # return render_template('index.html')
    return home()

@app.route('/movie')
def movie():
    datalist1 = []
    datalist2 = []
    datalist3 = []
    datalist4 = []
    datalist5 = []
    datalist6 = []
    datalist7 = []
    datalist8 = []
    datalist9 = []
    datalist10 = []
    con = sqlite3.connect('movie.db')
    cur = con.cursor()
    sql1 = "select * from movie250 where id between 1 and 25"
    sql2 = "select * from movie250 where id between 26 and 50"
    sql3 = "select * from movie250 where id between 51 and 75"
    sql4 = "select * from movie250 where id between 76 and 100"
    sql5 = "select * from movie250 where id between 101 and 125"
    sql6 = "select * from movie250 where id between 126 and 150"
    sql7 = "select * from movie250 where id between 151 and 175"
    sql8 = "select * from movie250 where id between 176 and 200"
    sql9 = "select * from movie250 where id between 201 and 225"
    sql10 = "select * from movie250 where id between 226 and 250"
    data1 = cur.execute(sql1)
    for item in data1:
        datalist1.append(item)
    cur.close()
    con.close()
    return render_template('movie.html',movies = datalist1)

@app.route('/score')
def score():
    score = []
    num = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(str(item[0]))
        num.append(item[1])
    cur.close()
    con.close()

    return render_template('score.html',score = score,num = num)

@app.route('/word')
def word():
    # con = sqlite3.connect('movie.db')
    # cur = con.cursor()
    # sql = "select instroduction from movie250"
    # data = cur.execute(sql)
    # text = ""
    # for item in data:
    #     text = text + item[0]
    # cur.close()
    # con.close()
    #
    # cut = jieba.cut(text)
    # string = ' '.join(cut)

    return render_template('word.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()
