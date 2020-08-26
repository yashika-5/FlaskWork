from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000
def index():
    return render_template('basic.html')


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
    return f"<h1>This is a page for {name.upper()}</h1>"


if __name__ == '__main__':
    app.run(debug=True)