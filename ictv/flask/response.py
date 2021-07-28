import flask

def seeother(url):
    return flask.redirect(url, code=303)

def badrequest(message=None):
    return flask.abort(400, message)

def forbidden(message=None):
    return flask.abort(403, message)

def notfound(message=None):
    return flask.abort(404, message)
