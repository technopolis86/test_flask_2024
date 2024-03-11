from flask import Flask, url_for, request, make_response, session
from flask_login import LoginManager


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')