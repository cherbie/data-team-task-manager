from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello World!'

if __name__ == '__app__':
    app.run(host='localhost', port=3000, debug=True)