import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    with open('index.html', 'rb') as f:
        data = f.read()
    return data

@app.route('/<filename>')
def getFile(filename):
    print(filename)
    with open(filename, 'rb') as f:
        data = f.read()
    return data

if __name__ == '__main__':
    app.run(    )