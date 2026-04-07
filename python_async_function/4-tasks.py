#!/usr/bin/env python3
"""Module that contains the task_wait_n function"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ A function that takes in 2 integer arguments
    (n and max_delay, with a default value of 10)
    named task_wait_n that returns a list of all the delays (float values)."""

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
