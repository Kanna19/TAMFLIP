from flask import g, render_template, request, url_for, Blueprint
from . import api_module

bp = Blueprint('subscribe', __name__, url_prefix="/subscribe")

@bp.route('/')
def index():
	# Sessions variables might be better
	if request.method == 'GET':
    # TODO
		return 'TODO'