import base
import logging
from fastapi import FastAPI, WebSocket

class Eval():
    ws: WebSocket = None

    class states:
        pass

    async def handle(self, ws):
        data = await ws.receive_text()
        logging.debug(data)
        self.ws = ws
        await base.__dict__[data.split(';')[0]].send_text(';'.join(data.split(';')[1:]))
    
    async def events(self, payload: tuple):
        pass

    async def send_text(self, text):
        await self.ws.send_text(text)

base.eval = Eval()

# example: elsa;/play_note;23;23