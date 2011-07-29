from pyramid.config import Configurator
from paste.httpserver import serve

from layout import default_globals_factory
from views import hello_world

if __name__ == '__main__':
    config = Configurator()
    config.add_view(hello_world, renderer="gumball:templates/index.pt")
    config.add_static_view('static', 'gumball:static/',
                           cache_max_age=86400)
    config.add_static_view('static-jslibs', 'jslibs:/',
                           cache_max_age=86400)
    config.set_renderer_globals_factory(default_globals_factory)
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')