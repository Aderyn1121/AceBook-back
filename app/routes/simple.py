from flask import Blueprint, redirect, render_template
from ..forms import NewInstrument
from ..models import Instrument, db

bp = Blueprint("simple", __name__, "")


@bp.route('/')
def simple():
    return render_template('main_page.html')
