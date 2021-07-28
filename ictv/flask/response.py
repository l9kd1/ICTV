import flask 

def created():
    return flask.make_response('201 Created', 201)

def nocontent():
    return flask.make_response('204 No Content', 204)

def seeother(url):
    return flask.redirect(url, 303)

def badrequest(message=None):
    return flask.make_response(message, 400)

def forbidden(message=None):
    return flask.make_response(message, 403)

def notfound(message=None):
    return flask.make_response(message, 404)

def nomethod():
    return flask.make_response('405 Method Not Allowed', 405)