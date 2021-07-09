import flask
from flask import Flask, session

def forbidden(message=None):
    return flask.make_response(message, code=403)

def seeother(url):
    return flask.redirect(url, code=303)
# Allows the use of the old rendering syntax previously used in web.py
class render_jinja:

    def __init__(self, *a, **kwargs):
        extensions = kwargs.pop('extensions', [])
        globals = kwargs.pop('globals', {})

        from jinja2 import Environment,FileSystemLoader
        self._lookup = Environment(loader=FileSystemLoader(*a, **kwargs), extensions=extensions)
        self._lookup.globals.update(globals)

    def __getattr__(self, name):
        path = name + '.html'
        t = self._lookup.get_template(path)
        return t.render

class Storage(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __repr__(self):
        return "<Storage " + dict.__repr__(self) + ">"

class FrankenFlask(Flask):

    def __init__(self,name):
        super().__init__(name)
        self.session = session
