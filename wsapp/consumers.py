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
            hello_msg = {
                "key":"default", # the key attributes will be used by client ws manager to route messages
                "content":"server says hello"
            }
            await self.send_json(hello_msg)
        except:
            await self.close()

    async def receive_json(self, content):
        # this method echos ws message back with timestamp
        print("message received")
        content['server_timestamp'] = int(time.time())
        content['key'] = 'default'
        await self.send_json(content)

    async def disconnect(self, code):
        # this method is called as a clean up
        print("connection" + str(self.scope) + "ended with error code" + str(code))
        pass
