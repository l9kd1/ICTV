from flask import Flask, session

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

class FrankenFlask(Flask):

    def __init__(self,name):
        super().__init__(name)
        self.session = session
