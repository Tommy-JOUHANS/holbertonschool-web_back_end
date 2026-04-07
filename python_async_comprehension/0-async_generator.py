#!/usr/bin/env python3
"""Module that contains a coroutine called async_generator
that takes no arguments."""


import asyncio
import random


async def async_generator():
    """Coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously
    wait 1 second for a random delay between 0 and 10, then yield
    the delay."""

    for _ in range(10):
        delay = random.uniform(0, 10)
        await asyncio.sleep(1.0)
        yield delay
