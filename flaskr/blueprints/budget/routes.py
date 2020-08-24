from flask import Blueprint


bp = Blueprint('budget', __name__, url_prefix='/budget')


@bp.route('/')
def index():
    return "budget index page updated in master"
