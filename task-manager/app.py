import os
from flask import Flask
from read_env import read_env
from tasks.views import tasks
from projects.views import projects

app = Flask(__name__)
read_env()

# @app.route('/')
# def helloWorld():
#    return 'Hello World!'

#app.add_url_rule('/', 'helloWorld', helloWorld)
app.register_blueprint(tasks)
app.register_blueprint(projects)

if __name__ == '__main__':
    app.run(host=os.environ['HOST'], port=os.environ['PORT'], debug=True)
