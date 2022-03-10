from flask import Flask, render_template, redirect
import flask_wtf
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm

app = Flask(__name__)


def main():
    db_session.global_init("db/mars.db")
    app.run(port=8080, host='127.0.0.1')


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs)
    return render_template("index.html", news=news)


@app.route('/training/<prof>')
def training(prof):
    prof.lower()
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<prof>')
def list_prof(prof=''):
    list = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач",
            "инженер по терраформированию", "климатолог", "специалист по радиационной защите",
            "астрогеолог", "гляциолог", "инженер жизнеобеспечения", "метеоролог",
            "оператор марсохода", "киберинженер", "штурман", "пилот дронов"
            ]
    return render_template('list_prof.html', prof=prof, list=list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {
        "Фамилия:": "Watny", "Имя:": "Mark", "Образование:": "выше среднего",
        "Профессия:": "штурман марсохода", "Пол:": "male",
        "Мотивация:": "Всегда мечтал застрять на Марсе!",
        "Готовы остаться на Марсе?": True
    }
    return render_template("auto_answer.html", data=data)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()