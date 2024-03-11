from flask import Flask, render_template, redirect, url_for
import json
from loginform import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=5)

@app.route('/boys')
def boys():
    return render_template('boys.html')

@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)




@app.route('/index/Заготовка')
def index_z():
    name = "И на Марсе будут яблони цвести!"
    return render_template('base.html', title='Домашняя страница',
                           site_name=name)

@app.route('/training/<prof>')
def traning(prof):
    return render_template('traning.html', prof=prof.lower())



@app.route('/list/<arg>')
def spisok(arg):
    return render_template('list.html', arg=arg)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')