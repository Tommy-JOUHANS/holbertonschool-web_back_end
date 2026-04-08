#!/usr/bin/env python3
"""Module that contains a coroutine called async_generator
that takes no arguments.
The coroutine will loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10.
Use the random module."""


import random
import asyncio
import time


async def async_generator():
    """Coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10.
    Use the random module."""

    for delay in range(10):
        delay = asyncio.create_task(asyncio.sleep(1))
        await delay
        yield random.uniform(0, 10)
