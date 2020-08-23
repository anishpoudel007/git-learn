from flask import Blueprint


bp = Blueprint('public', __name__)


@bp.route('/')
def home():
    return "home page"
