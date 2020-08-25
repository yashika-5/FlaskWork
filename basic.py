from flask import Flask

app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000
def index():
    return "<h1>Hello World</h1>"

@app.route('/info') # 127.0.0.1:5000/info
def info():
    return "<h1>Information page</h1>"


@app.route('/users_data/<name>')
def user(name):
    return f"<h1>This is a page for {name.upper()}</h1>"

if __name__ == '__main__':
    app.run()