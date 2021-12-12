from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h style="color:blue;font-size:40px;">Hello Flask World! ^^</h1>'


@app.route('/user/<name>')
def user(name):
    return f'<h style="color:blue;font-size:40px;">Hello, {name}!</h1>'


if __name__ == '__main__':
    app.run(debug=True)