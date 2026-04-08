#!/usr/bin/env python3


import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension
from typing import List


async def measure_runtime() -> List[float]:
    """Coroutine called measure_runtime that takes no arguments.
    The coroutine will execute async_comprehension four times in
    parallel using asyncio.gather and return the total runtime."""

    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = asyncio.get_event_loop().time()

    return end_time - start_time
