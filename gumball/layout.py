from pyramid.decorator import reify
from pyramid.url import static_url

class API(object):
    """ All 'API' objects are used by renderer_globals_factory """
    def __init__(self, context, request):
        self.context = context
        self.request = request

class URLAPI(API):

    gonzo = "91232"
    @reify
    def context_url(self):
        return resource_url(self.context, self.request)

    @reify
    def app_url(self):
        return self.request.application_url

    @reify
    def app_static(self):
        # TODO need a way to get 'gumball' via a call
        return static_url('gumball:static/', self.request)

    @reify
    def deform_static(self):
        return static_url('deform:static/', self.request)

    @reify
    def jslibs_static(self):
        return static_url('jslibs:static/', self.request)

def default_globals_factory(system):
    request, context = system['request'], system['context']
    return {
        'url':URLAPI(context, request),
        }
