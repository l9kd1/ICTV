import flask 

def seeother(url):
    return flask.redirect(url, code=303)

def badrequest(message=None):
    return flask.make_response(message, code=400)

def forbidden(message=None):
    return flask.make_response(message, code=403)

def notfound(message=None):
    return flask.make_response(message, code=404)