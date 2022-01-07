from flask import request
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    # return '<p>Your browser is %s</p>' %user_agent
    return f'<p>Your browser is {user_agent}</p>'


if __name__ == '__main__':
    app.run(debug=True)
