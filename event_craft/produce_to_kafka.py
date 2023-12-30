import asyncio
import websockets


async def consume_websocket(url):
    async with websockets.connect(url) as websocket:
        while True:
            event_data = await websocket.recv()
            # Process or send the data to Kafka here
            print(f"Received WebSocket event: {event_data}")

asyncio.get_event_loop().run_until_complete(consume_websocket("ws://example.com/socket"))


