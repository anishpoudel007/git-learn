from flask import Blueprint


bp = Blueprint('public', __name__)


@bp.route('/')
def home():
    return "home page updated response"


@bp.route('/about-us')
def about():
    return "about us page"
