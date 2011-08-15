#
# This is the magic chant you have to do in your view code, unless
# we find a way to eliminate it
#
from pyramid.events import subscriber
from pyramid.events import BeforeRender

from gumball.layout import LayoutManager

@subscriber(BeforeRender)
def add_renderer_globals(event):
    system = event._system
    request, context = system['request'], system['context']
    event['layout'] = LayoutManager(context, request)

#
# Then this is your normal view code
#
from pyramid.view import view_config

@view_config(renderer="gumball:sample/templates/index.pt")
def index_view(request):
    return {"project": "Some Project"}
