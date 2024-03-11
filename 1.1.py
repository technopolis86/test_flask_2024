from flask import Flask, url_for

app = Flask(__name__)

lst = [
    'Человечество вырастает из детства',
    'Человечеству мала одна планета.',
    'Мы сделаем обитаемыми безжизненные пока планеты.',
    'И начнем с Марса!',
    'Присоединяйся!'
]



@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index1():
    return "<h1>И на Марсе будут яблони цвести!</h1>"

@app.route('/promotion')
def promotion():
    return "</br>".join(lst)




if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')