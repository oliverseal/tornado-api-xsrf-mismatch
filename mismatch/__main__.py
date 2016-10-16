import os.path
import asyncio
import tornado.web
import tornado.ioloop
import tornado.netutil
import tornado.process
from tornado.httpserver import HTTPServer
from tornado.platform.asyncio import AsyncIOMainLoop

from mismatch.handlers import *

def main():
    routes = [
        # api request handler
        (r'/api/', APIHandler),
        # page
        (r'/', PageHandler),
    ]

    tornado_settings = {
        'xsrf_cookies': True,
        'serve_traceback': True,
        'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    }

    # tornado.process.fork_processes(2)
    AsyncIOMainLoop().install()
    app = tornado.web.Application(routes, debug=True, **tornado_settings)

    server = HTTPServer(app)
    server.add_sockets(tornado.netutil.bind_sockets(8000))
    loop = asyncio.get_event_loop()
    loop.run_forever()

if __name__ == '__main__':
    main()