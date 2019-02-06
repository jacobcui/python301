
from flask import Flask, render_template, request
import db
import auth
import blog
import simple

app = Flask(__name__)

app.config.from_pyfile('config.py', silent=True)

app.register_blueprint(auth.bp)
app.register_blueprint(blog.bp)
app.register_blueprint(simple.bp)

app.add_url_rule('/', endpoint='index')

db.init_app(app)

# Set following environment variables in command line:
# set FLASK_APP=server.py
# set FLASK_ENV=development
# Or if use pycharm, set these variables in run configuration.

# To set up the database,
# Right click this file, opens a terminal
# In the command line, set the env variable:
#   set FLASK_APP=server.py
# Then run following command.
#   flask init-db


@app.route('/version', methods=['GET', 'POST'])
def version_handler():
    if request.method == 'GET':
        return render_template('version.html')


if __name__ == '__main__':
    app.run()
