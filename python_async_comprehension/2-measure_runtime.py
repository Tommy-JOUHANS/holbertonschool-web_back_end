#!/usr/bin/env python3


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine called measure_runtime that takes no arguments.
    The coroutine will execute async_comprehension four times in
    parallel using asyncio.gather, then return the total runtime."""

    start_time = time.perf_counter()
    measure = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*measure)
    end_time = time.perf_counter()
    return end_time - start_time
