# Application Factory
import os
from flask import Flask
from flask import render_template
from flask import request, g

from . import api_module
from . import flight_tracker

from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from pytz import utc


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'tamflip.sqlite'),

    )
    # to add zip functionality to jinja
    app.jinja_env.globals.update(zip=zip)

    # Ensure instance folder exists
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

    # Link scheduler
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        scheduler = BackgroundScheduler(
            jobstores=jobstores,
            executors=executors,
            job_defaults=job_defaults,
            timezone=utc
        )
        # Add a cron job which gets triggered every day at 0330 UTC.
        scheduler.add_job(
            flight_tracker.send_alerts_to_subscribed_users,
            trigger='cron',
            args=[app],
            hour='3',
            minute='30'
        )
        scheduler.start()

    # Link with Database
    from . import db
    db.init_app(app)

    # Link blueprints
    from . import index
    app.register_blueprint(index.bp)

    from . import subscribe
    app.register_blueprint(subscribe.bp)

    return app
