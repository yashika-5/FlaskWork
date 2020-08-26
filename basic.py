from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000
def index():
    user_logged_in = True
    return render_template('basic.html', user_logged_in=user_logged_in)


@app.route('/info')  # 127.0.0.1:5000/info
def info():
    name = 'yashika'
    letters = list(name)
    mylist = ['rufus','fluffy','spiky']
    mydictionary = {'name': 'Jose'}
    some_variable = "Dude"
    return render_template('tmp_basic.html', my_var=some_variable, letters=letters, mydictionary=mydictionary, mylist=mylist)


@app.route('/users_data/<name>')
def user(name):
    if name == 'john':
        user_logged_in = True
    else:
        user_logged_in = False
    return render_template('loggedIn.html', name=name, user_logged_in=user_logged_in)


if __name__ == '__main__':
    app.run()