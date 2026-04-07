#!/usr/bin/env python3
"""Module that contains asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10)
named wait_random that waits for a random delay
between 0 and max_delay (included and float value)
seconds and eventually returns it"""


import asyncio
import random


async def wait_random(min_delay=0, max_delay=10) -> float:
    """Wait for a random delay between 0
    and max_delay (inclusive) and return it.

    Args:
        max_delay (int, optional):
        The maximum delay in seconds. Defaults to 10.
        min_delay (int, optional):
        The minimum delay in seconds. Defaults to 0.

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(min_delay, max_delay)
    await asyncio.sleep(delay)
    return delay
