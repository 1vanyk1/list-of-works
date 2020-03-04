from flask import Flask, render_template, redirect, request
from PIL import Image
import json
import os
import random
import codecs
from data import db_session
from data.jobs import Jobs
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def home_page():
    param = {}
    db_session.global_init("db/blogs.sqlite")
    session = db_session.create_session()
    for job in session.query(Jobs).all():
        param['jobs'] = param.get('jobs', []) + [[job.id, job.job, job.team_leader, job.work_size, job.collaborators, job.is_finished]]
        # param['id'] = param.get('id', []) + [job.id]
        # param['title'] = param.get('title', []) + [job.job]
        # param['team_leader'] = param.get('team_leader', []) + [job.team_leader]
        # param['duration'] = param.get('duration', []) + [job.work_size]
        # param['collaborators'] = param.get('collaborators', []) + [job.collaborators]
        # param['is_finished'] = param.get('is_finished', []) + [job.is_finished]
    return render_template('list_of_jobs.html', **param)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
