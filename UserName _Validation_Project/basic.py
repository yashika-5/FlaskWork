from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report_fun():
    username = request.args.get('username')
    upper_letter = any(s.isupper() for s in username)
    lower_letter = any(s.islower() for s in username)
    end_digit = username[-1].isdigit()
    report = upper_letter and lower_letter and end_digit
    return render_template('report.html',report=report, upper=upper_letter, lower=lower_letter, last=end_digit)


if __name__ == '__main__':
    app.run()