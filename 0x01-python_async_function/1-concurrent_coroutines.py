#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async """
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ return the list of all the delays """
    ls = []
    for _ in range(n):
        t = await wait_random(max_delay)
        if len(ls) == 0:
            ls.append(t)
            continue
        elif len(ls) == 1:
            if t > ls[0]:
                ls.append(t)
            else:
                ls.insert(0, t)
        else:
            c = 0
            for i in ls:
                if t > ls[c]:
                    c += 1
                    if c == len(ls):
                        ls.append(t)
                        break
                    continue
                else:
                    ls.insert(c, t)
                    break
    return ls
