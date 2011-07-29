from pyramid.renderers import get_renderer

def hello_world(request):
    layout = get_renderer('templates/layout.pt').implementation()
    return {"project": "Some Project", "layout": layout}

def fluid(request):
    return {"title": "Fluid layout"}
