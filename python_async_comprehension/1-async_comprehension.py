#!/usr/bin/env python3
"""Module that contains a coroutine called
async_comprehension that takes no arguments."""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Coroutine called async_comprehension that takes no arguments.
    The coroutine will collect 10 random delays using an async
    comprehensing over async_generator, then return the 10 delays."""

    delays = [delay async for delay in async_generator()]
    return delays
