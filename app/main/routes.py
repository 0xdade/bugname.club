from flask import redirect, url_for, flash, render_template

from app.main import bp

@bp.route('/')
@bp.route('/<string:cve>')
def index(cve=None):
    if cve:
        return render_template('main.html', cve=cve)

    return render_template('main.html')