from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def i():
    return '''<!doctype html>
                <body>
                  <h1>Миссия Колонизация Марса</h1>
                </body>'''


@app.route('/index')
def index():
    return '''<!doctype html>
                <body>
                  <h1>И на Марсе будут яблони цвести!</h1>
                </body>'''


@app.route('/promotion_image')
def image_mars():
    return f'''<!doctype html>
                <head>
                  <meta charset="utf-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                  <link rel="stylesheet" 
                  href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                  integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                  crossorigin="anonymous">
                  <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                  <title>Привет, Марс!</title>
                </head>
                <body>
                  <h1>Жди нас, Марс!</h1>
                  <img src="{url_for('static', filename='img/mars.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась" hspace="15">
                  <div class="alert alert-primary" role="alert">
                    Человек вырастает из детства.
                  </div>
                  <div class="alert alert-secondary" role="alert">
                    Человеку мала одна планета.
                  </div>
                  <div class="alert alert-success" role="alert">
                    Мы сделаем обитаемыми безжизненные пока планеты.
                  </div>
                  <div class="alert alert-danger" role="alert">
                    И начнём с марса!
                  </div>
                  <div class="alert alert-warning" role="alert">
                    Присоединяйся!
                  </div>
                </body>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1 align="center">Анкета претендента</h1>
                                <h2 align="center">на участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                        <input type="name" class="form-control" id="password" placeholder="Введите имя" name="name">
                                        <label for="about"></label>
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у Вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное общее</option>
                                              <option>Основное общее</option>
                                              <option>Среднее общее</option>
                                              <option>Начальное профессиональное</option>
                                              <option>Среднее профессиональное</option>
                                              <option>Высшее профессиональное</option>
                                            </select>
                                         </div>
                                         <label for="professions">Какие у вас есть профессии?</label>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="ing-f" name="accept">
                                            <label class="form-check-label" for="ing-f">Инженер-исследователь</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="ing-build" name="accept">
                                            <label class="form-check-label" for="ing-build">Инженер-строитель</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="pilot" name="accept">
                                            <label class="form-check-label" for="pilot">Пилот</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="meteor" name="accept">
                                            <label class="form-check-label" for="meteor">Метеоролог</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="life-ing" name="accept">
                                            <label class="form-check-label" for="life-ing">Инженер по жизнеобеспечению</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="radioactive" name="accept">
                                            <label class="form-check-label" for="radioactive">Инженер по радиационной защите</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="doc" name="accept">
                                            <label class="form-check-label" for="doc">Врач</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="eco" name="accept">
                                            <label class="form-check-label" for="eco">Экобиолог</label>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <br>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <br>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
