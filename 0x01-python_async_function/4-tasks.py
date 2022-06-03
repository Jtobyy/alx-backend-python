#!/usr/bin/env python3
""" Tasks """
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> asyncio.Task:
    '''identical to wait_n except task_wait_random is being called.'''
    ls = []
    for _ in range(n):
        t = await task_wait_random(max_delay)
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
