from flask import  Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f"simple routing welcome page"

@app.route('/dynamic/<name>') # dynamic routing = localhost:5000/Play or /Huff
def puppylatin(name):
    if name[-1] != 'f':
       name = "".join([name,'y'])
    else:
      name = "".join([name,'ful'])
    return f"<h1>This is a page for dynamic routing : {name}</h1>"

if __name__ == '__main__':
    app.run()


