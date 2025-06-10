from flask import (
    Blueprint, flash, render_template, request, url_for
)

bp = Blueprint('base_views', __name__, url_prefix='/')

@bp.route('/', methods=('GET',))
def idx_main():
    return render_template('index_page.html')
