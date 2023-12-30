import json
import asyncio
import websockets
import time

# WebSocket URL (use "ws" for unencrypted connection)
websocket_url = "ws://0.0.0.0:8765"


async def generate_event():
    # Replace this with your actual event generation logic
    event = {
        "user_id": "e51c50df-8713-48b6-8be5-fefafbbbdfef",
        "event_time": "2023-12-17T19:54:20.344591",
        "server_upload_time": "2023-12-17T19:54:35.277720",
        "client_upload_time": "2023-12-17T19:54:36.268530",
        "event_name": "spline_added",
        "platform": "macOS",
        "country_code": "MN",
        "app_store_country": "MNG",
    }
    return json.dumps(event)


async def send_events(websocket, path):
    while True:
        event = await generate_event()

        # Send the generated event
        await websocket.send(event)

        # Wait for a short interval before sending the next event
        await asyncio.sleep(2)


if __name__ == "__main__":
    start_server = websockets.serve(send_events, "0.0.0.0", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
