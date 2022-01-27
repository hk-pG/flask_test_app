from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'


@app.route('/ja')
def hello_ja():
    return '<h1>ちっす</h1>'


if __name__ == '__main__':
    app.run()
