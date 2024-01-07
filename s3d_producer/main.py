import csv
import json
import asyncio
import websockets
from deh.poisson import PoissonTriggerGenerator
from deh.events import RandomEventGenerator
import random
import numpy as np

RATE = 20

random.seed(24)
np.random.seed(24)

with open("deh/country_codes.csv", "r") as file:
    country_codes = list(csv.reader(file))[1:]

with open("deh/tracking_ids.json", "r") as file:
    tracking_ids = json.load(file)


async def serve(websocket, _):
    event_generator = RandomEventGenerator(
        country_codes=country_codes, tracking_ids=tracking_ids
    )
    p = PoissonTriggerGenerator(event_generator.get_event, RATE)

    await p.start()
    async for event in p.get():
        try:
            await websocket.send(json.dumps(event, default=str))
        except websockets.exceptions.ConnectionClosedError:
            return


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start_server = websockets.serve(serve, "0.0.0.0", 8765)
    loop.run_until_complete(start_server)
    loop.run_forever()
