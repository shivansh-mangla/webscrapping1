from flask import Flask, render_template
import jinja2
import database as db

app = Flask(__name__)
news_data, jobs_data, last_update = [], [], []

@app.route('/')
def hello():
    global news_data
    global jobs_data
    global last_update
    news_data, jobs_data, last_update = db.load_data()
    return render_template('index.html', news_data=news_data, jobs_data=jobs_data, last_update=last_update)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
