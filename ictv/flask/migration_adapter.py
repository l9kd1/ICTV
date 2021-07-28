import flask
from flask import Flask, session
from werkzeug.middleware.dispatcher import DispatcherMiddleware

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
        self.plugins = {}
        self.pre_processors = []
        self.post_processors = []
        self.error_handlers = []
        self.appset = set()

    def register_plugin(self,route,app):
        """
            Register sub applications to provision the dispatcher.
        """
        # Copying the ictv_app config
        tmp_config = self.config.copy()
        tmp_config.update(app.config)
        app.config = tmp_config

        # Copying the plugin manager
        app.plugin_manager = self.plugin_manager

        # Copying the slide renderer
        app.ictv_renderer = self.ictv_renderer

        # Duplicating the secret_key to make the session accessible
        # WARN: MUST be the same as self.secret_key
        app.secret_key = self.secret_key

        self.plugins[route] = app
        self.appset.add(app)

    def get_app_dispatcher(self):
        """
            Initialize the dispatcher with the default app
            and the plugin sub-apps as mounts with
            specific root paths in their urls
        """
        self.apply_pre_processors()
        self.apply_post_processors()
        self.apply_error_handlers()

        dispatcher = DispatcherMiddleware(self,self.plugins)
        dispatcher.config = self.config
        return dispatcher

    def register_before_request(self,factory,cascade=False,needs_app=False):
        """
            Save preprocessors factories in order to apply them
            just before initializing the DispatcherMiddleware.
            @params : - function factory: processor factory
                      - bool cascade: whether this must be applied to the plugins
                      - bool needs_app: whether the factory needs the app instance

        """
        self.pre_processors.append({"factory":factory,"cascade":cascade,"needs_app":needs_app})

    def register_after_request(self,factory,cascade=False,needs_app=False):
        """
            Save postprocessors factories in order to apply them
            just before initializing the DispatcherMiddleware.
            @params : - function factory: processor factory
                      - bool cascade: whether this must be applied to the plugins
                      - bool needs_app: whether the factory needs the app instance

        """
        self.post_processors.append({"factory":factory,"cascade":cascade,"needs_app":needs_app})

    def prepare_error_handler(self,error,factory,cascade=True,needs_app=False):
        """
            Save error handlers in order to register them with app.register_error_handler()
            just before initializing the DispatcherMiddleware.
            @params : - Exception error: the error to be handled
                      - func handler: the handler factory
                      - bool cascade: whether this must be applied to the plugins
                      - bool needs_app: whether the factory needs the app instance

        """
        self.error_handlers.append({"error":error,"handler_factory":factory, "cascade":cascade, "needs_app":needs_app})

    def apply_pre_processors(self):
        """
            Calls the before_request for each app instance
        """
        for proc in self.pre_processors:
            self.before_request(proc["factory"]() if not proc["needs_app"] else proc["factory"](self))
            if proc["cascade"]:
                for value in self.appset:
                    value.before_request(proc["factory"]() if not proc["needs_app"] else proc["factory"](value))

    def apply_post_processors(self):
        """
            Calls the after_request for each app instance
        """
        for proc in self.post_processors:
            self.after_request(proc["factory"]() if not proc["needs_app"] else proc["factory"](self))
            if proc["cascade"]:
                for value in self.appset:
                    value.after_request(proc["factory"]() if not proc["needs_app"] else proc["factory"](value))

    def apply_error_handlers(self):
        """
            Calls the register_error_handler for each app instance
        """
        for proc in self.error_handlers:
            self.register_error_handler(proc["error"],proc["handler_factory"]() if not proc["needs_app"] else proc["handler_factory"](self))
            if proc["cascade"]:
                for value in self.appset:
                    value.register_error_handler(proc["error"],proc["handler_factory"]() if not proc["needs_app"] else proc["handler_factory"](value))
