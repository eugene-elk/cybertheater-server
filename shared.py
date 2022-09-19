import logging, typing

class Base():

    def __init__(self):
        self.ws = None

    async def handler(self, data):
        logging.debug(f"{type(self)} handler received data: {data}")
        self.events(data.lower().split())
    
    async def events(self, payload: tuple):
        pass

gestures = robert = elsa = seldon = Base()
