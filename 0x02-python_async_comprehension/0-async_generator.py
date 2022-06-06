#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random


async def async_generator():
    """ Asynchronously yield a random number between 0 and 10 """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
