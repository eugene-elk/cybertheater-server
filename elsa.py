import base
import logging

class Elsa(base.Base):
    async def events(self, payload: tuple):
        event = payload[0][1:]
        match event:
            case "panic":
                await base.seldon.send_text("Hello, Elsa")
            case "hands_up":
                pass

base.elsa = Elsa()