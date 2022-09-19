import logging, typing
from fastapi import FastAPI, WebSocket

class Base():
    
    ws: WebSocket = None

    class states:
        pass

    async def handle(self, ws):
        data = await ws.receive_text()
        logging.debug(data)
        data = data.lower()
        self.ws = ws
        await self.events(data.split(';')) # TODO split by ;
    
    async def events(self, payload: tuple):
        pass

    async def send_text(self, text):
        await self.ws.send_text(text)

gestures, robert, elsa, seldon, robertHands, eval = None, None, None, None, None, None