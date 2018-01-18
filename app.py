from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return "Welcome to the homepage"


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='visitor'):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
