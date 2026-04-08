#!/usr/bin/env python3


import asyncio

from typing import runtime_checkable


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine called measure_runtime that takes no arguments.
    The coroutine will execute async_comprehension four times in
    parallel using asyncio.gather, then return the total runtime."""

    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = asyncio.get_event_loop().time()

    return end_time - start_time
