import flask

def created():
    return flask.make_response('201 Created', 201)

def nocontent():
    return flask.abort(204, '204 No Content')

def seeother(url):
    return flask.redirect(url, 303)

def badrequest(message=None):
    return flask.abort(400, message)

def forbidden(message=None):
    return flask.abort(403, message)

def notfound(message=None):
    return flask.abort(404, message)

def nomethod():
    return flask.abort(405,'405 Method Not Allowed')