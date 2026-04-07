#!/usr/bin/env python3
""" A function that takes in an integer argument
(max_delay, with a default value of 10)
named task_wait_random that returns a asyncio.Task"""

import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A function that takes in an integer argument
    (max_delay, with a default value of 10)
    named task_wait_random that returns a asyncio.Task
    The function should be a 2-arg wrapper for wait_random"""
    return asyncio.Task(wait_random(max_delay))
