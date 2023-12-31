import random
import math
import asyncio

class PoissonTriggerGenerator:
    def __init__(self, func, time):
        self.func = func
        self.time = time
        self.is_started = False

    async def start(self):
        self.is_started = True

    async def get(self):
        while self.is_started:
            arrival_time = self._poisson_arrival()
            await asyncio.sleep(arrival_time)
            yield self.func()

    def stop(self):
        if self.is_started:
            self.is_started = False

    def _poisson_arrival(self):
        # Get the next probability value from Uniform(0,1)
        p = random.random()

        # Plug it into the inverse of the CDF of Exponential(_lambda)
        return -math.log(1.0 - p) / self.time
