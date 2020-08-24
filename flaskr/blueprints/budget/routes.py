from flask import Blueprint


bp = Blueprint('budget', __name__)


@bp.route('/')
def index():
    return "budget index page"
