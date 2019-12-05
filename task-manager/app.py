from flask import Flask
from tasks import views

app = Flask(__name__)

# @app.route('/')
# def helloWorld():
#    return 'Hello World!'

#app.add_url_rule('/', 'helloWorld', helloWorld)
app.register_blueprint(views.tasks)

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
