from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

bp = Blueprint('database', __name__, url_prefix='/database')


@bp.route('/')
def hello():
    return "<h1>Database</h1><br><p>this module is for accessing the Database</p>"


@bp.route('/users')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)
