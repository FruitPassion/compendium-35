from functools import wraps

from flask import session, redirect, url_for


ACTION_INDEX = "auth.choix_connexion"


def logout_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get("nom_compte"):
            return redirect(url_for('auth.logout'))
        return func(*args, **kwargs)
    return decorated_function
