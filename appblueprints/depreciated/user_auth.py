import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

# need to import the database object.


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/')
def hello():
    return "<h1>AUTH</h1><br><p>this module is for User Login and Registration </p>"
