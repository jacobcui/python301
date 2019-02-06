import flask
import datetime
print(flask.__version__)
print(__file__)
app = flask.Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/get_time')
def get_time():
    now_string = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    a_list = ['hello', 'world']
    a_list_dict = [
        {'title': 'Software engineer', 'name': 'Bob'},
        {'title': 'HR manager', 'name': 'Tom'},
    ]
    return flask.render_template(
        'index.html',
        current_time=now_string,
        words=a_list,
        stuff_list=a_list_dict
    )

app.run()