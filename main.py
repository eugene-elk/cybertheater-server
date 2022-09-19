# To start: "C:\Users\Лосицкий Игорь\AppData\Local\Programs\Python\Python310\python.exe" -m uvicorn main:app --port 80 --host 0.0.0.0

import ascii_art
import base
import robert, gestures, robert_hands, eval, elsa
import typing, logging
from fastapi import FastAPI, WebSocket

app = FastAPI()
logging.basicConfig(level=logging.DEBUG)

@app.websocket("/ws/{id}")
async def ws_handler(ws: WebSocket,  id: str):
    await ws.accept()
    while True:
        await base.__dict__[id].handle(ws)