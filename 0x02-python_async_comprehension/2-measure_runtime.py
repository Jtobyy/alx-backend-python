#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure total runtime and returns it """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(3)))
    return time.perf_counter() - start
