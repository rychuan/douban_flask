from flask import Flask,render_template
import sqlite3

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
    datalist = []
    con = sqlite3.connect('movie.db')
    cur = con.cursor()
    sql1 = "select * from movie250 where id between 1 and 25"
    sql2 = "select * from movie250 where id between 26 and 50"
    data = cur.execute(sql2)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template('movie.html',movies = datalist)

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/word')
def word():
    return render_template('word.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run()
