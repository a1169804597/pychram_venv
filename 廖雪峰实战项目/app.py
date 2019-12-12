import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
	return web.Response(body = b"<h1>Hi, there!</h1>", headers = {"content-type": "text/html"})



async def init(loop):
	app = web.Application()
	app.add_routes([web.get("/", index)])
	srv = await loop.create_server(web.AppRunner(app), "127.0.0.1", 9090)
	logging.info("the server started")
	return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()