from flask import Blueprint


bp = Blueprint('database', __name__, url_prefix='/database')


@bp.route('/')
def hello():
    return "<h1>Database</h1><br><p>this module is for accessing the Database</p>"
