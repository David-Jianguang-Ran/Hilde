from channels.generic.websocket import AsyncJsonWebsocketConsumer

import time


class LiveConsumer(AsyncJsonWebsocketConsumer):
    # this is the boiler plate consumer for handling websocket connections
    async def connect(self, text_data=None, bytes_data=None):
        print("ws connection initiated")
        # currently only accept when subprotocol is matched
        try:
            await self.accept()
            print("ws connection established")
        except:
            await self.close()

    async def receive_json(self, content):
        # this method echos ws message back with timestamp
        content['server_timestamp'] = int(time.time())
        await self.send_json(content)

    async def disconnect(self, code):
        # this method is called as a clean up
        print("connection" + str(self.scope) + "ended with error code" + str(code))
        pass
