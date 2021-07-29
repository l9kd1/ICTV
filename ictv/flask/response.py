import flask

def seeother(url):
    flask.abort(flask.redirect(url, code=303))

def badrequest(message=None):
    flask.abort(400, message)

def forbidden(message=None):
    flask.abort(403, message)

def notfound(message=None):
    flask.abort(404, message)
