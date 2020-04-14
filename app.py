import aiohttp
import aiohttp_jinja2
import jinja2

from aiohttp import web

class Server(web.Application):

    def __init__(self):
        super().__init__()

        self.add_routes([
            web.static('/static', 'static'),
            web.get('/', self.index)
        ])

    @aiohttp_jinja2.template('core.jinja2')
    async def index(self, request: web.Request):
        return {}

if __name__ == "__main__":
    app = Server()
    
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

    web.run_app(app, host='localhost', port=8081)