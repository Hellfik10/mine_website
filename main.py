from flask import Flask, render_template, redirect
import flask_wtf
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm
from forms.JobsForms import JobsForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms.LoginForm import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "12Qwdc#d%32"
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/mars.db")
    app.run(port=8080, host='127.0.0.1')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs)
    users = db_sess.query(User).all()
    name = {}
    for i in news:
        for j in range(len(users)):
            if i.team_leader == j + 1:
                name[i.team_leader] = users[j]
                break
    return render_template("index.html", news=news, name=name)


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
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/addjob',  methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()
        job.job = form.title.data
        job.team_leader = form.team_leader.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.is_finished.data
        db_sess.merge(job)
        db_sess.commit()
        return redirect('/')
    return render_template('addjob.html', title='Добавление новости',
                           form=form)


if __name__ == '__main__':
    main()