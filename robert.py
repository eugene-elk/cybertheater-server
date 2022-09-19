import base
import logging

class Robert(base.Base):
    async def events(self, payload: tuple):
        event = payload[0][1:]
        match event:
            case "gesture_detected":
                await base.seldon.send_text("Hello, Robert")
            case "hands_up":
                pass

base.robert = Robert()