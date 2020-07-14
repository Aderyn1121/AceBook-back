from flask import Blueprint, request, jsonify
import jwt

from ..models import db
from ..config import Configuration

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route('/')
def simple():
    return render_template('main_page.html')
