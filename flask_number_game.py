from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return f'<b>{func()}'

    return wrapper


def make_emphasis(func):
    def wrapper():
        return f'<em>{func()}'

    return wrapper


def make_underlined(func):
    def wrapper():
        return f'<u>{func()}'

    return wrapper


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/bye')
def bye():
    return 'Goodbye!'


@app.route('/username/<name>/1')
def greet(name):
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run(debug=True)
