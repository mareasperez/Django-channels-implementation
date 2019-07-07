from channels.generic.websocket import AsyncJsonWebsocketConsumer

class DataConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip2", self.channel_name)
        print(f"Added {self.channel_name} channel to gossip2")

    async def disconnect(self):
        await self.channel_layer.group_discard("gossip2", self.channel_name)
        print(f"Removed {self.channel_name} channel to gossip2")

    async def data_new(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")
