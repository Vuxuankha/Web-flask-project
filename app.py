from flask import Flask, render_template, jsonify
from database import load_jobs_fromdb

app = Flask(__name__)


@app.route('/')
def hello_world():
  jobs = load_jobs_fromdb()
  return render_template('home.html', job=jobs, company_name='kha')


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
