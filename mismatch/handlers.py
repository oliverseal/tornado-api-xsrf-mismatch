import json
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        force_xsrf_cookie = self.xsrf_token
        print('Token for {}: {}'.format(self.request.uri, force_xsrf_cookie))

class PageHandler(BaseHandler):
    def get(self):
        context = {}
        return self.render('page.html', **context)


# this is actually in a separate file usually
class APIHandler(BaseHandler):
    SUPPORTED_METHODS = ['POST']

    async def post(self, *args, **kwargs):
        request_data = json.loads(self.request.body)
        if request_data['method'] == 'derp':
            return json.dumps({
                'id': request_data['id'],
                'result': 'werp'
            })