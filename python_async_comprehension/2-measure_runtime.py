#!/usr/bin/env python3


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        measure time and execute in paralallel

        Args:
            void

        Return:
            float random numbers
  """
    start_time = time.perf_counter()
    measure = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*measure)
    end_time = time.perf_counter()
    return (end_time - start_time)
