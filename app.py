from aiohttp import web
import aiohttp_jinja2

class Server(web.Application):

    def __init__(self):
        super().__init__()

        self.add_routes([
            web.static('/static', static),
            web.get('/', self.index)
        ])

    @aiohttp_jinja2.template('core.jinja2')
    async def index(self, request: web.Request):
        return {}
