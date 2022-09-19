import base
import logging
import time 

async def playfile(ws, filename):
    with open(filename) as f:
        for line in f.read().split('\n'):
            # if 'delay' in line:
            time.sleep(0.01)
            #     continue
            await ws.send_text(line)
            print(line)
            # time.sleep(int(line.split(';')[1]) / 1000)


class Gestures(base.Base):
    async def events(self, payload: tuple):
        payload = payload[0].split()
        event = payload[0][1:].lower() # TODO move in base
        event = event.replace('received', 'gesture_detected') # TODO remove deprecated api
        match event:
            case "gesture_detected":
                gesture = payload[1].replace("gestures.", '') # TODO remove legacy
                logging.info(f"Detected gesture {gesture}")
                match gesture:
                    case "one":
                        await playfile(base.robertHands, 'paris-rs.txt')
                        # await base.robertHands.send_text("/move_servo;90") # TODO separate method for command sending
                    case "two": # TODO rename tree to three
                        await playfile(base.robertHands, 'canary-rs.txt')
                    case "rock":
                        await base.robert.send_text("/prepare")
                    # case "one":
                    #     await base.robertHands.send_text("/move_servo;0")
            case "hands_up":
                pass
            case "test":
                logging.info('Starting robertHands...')
                await base.robertHands.send_text("/start")


base.gestures = Gestures()