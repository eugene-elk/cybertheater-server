import base
import logging

class RobertHands(base.Base):
    async def events(self, payload: tuple):
        event = payload[0][1:]
        match event:
            case "gesture_detected":
                await base.robert.send_text("/say Hello, Robert")
            case "start":
                logging.info('Starting RobertHands')
                base.robert.send_text("/say Hello, Robert")
base.robertHands = RobertHands()