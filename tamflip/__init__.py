#Application Factory
import os
from flask import Flask
from flask import render_template
from flask import request, g
from . import apiModule

from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from pytz import utc


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': '__init__:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 5
        }
    ]

    SCHEDULER_JOBSTORES = {
        'default': MemoryJobStore()
    }

    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 20}
    }

    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 3
    }

    SCHEDULER_API_ENABLED = True


def job1():
    print("DID JOB!!")

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'tamflip.sqlite'),

    )

    #ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    jobstores = {'default':MemoryJobStore()}
    executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
    }
    job_defaults = {
        'coalesce': False,
        'max_instances': 3
    }

    #Link scheduler
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
        scheduler.add_job(job1, 'interval', seconds=5)
        scheduler.start()

    # Link with Database
    from . import db
    db.init_app(app)

    #Link blueprints
    from . import index
    app.register_blueprint(index.bp)

    return app
