from pyramid.events import subscriber
from pyramid.events import BeforeRender
from pyramid.view import view_config

from gumball.layout import LayoutManager

@subscriber(BeforeRender)
def add_renderer_globals(event):
    system = event._system
    request, context = system['request'], system['context']
    event['layout'] = LayoutManager(context, request)

@view_config(renderer="bottlecap:sample/templates/index.pt")
def index_view(request):
    return {"project": "Some Project"}
