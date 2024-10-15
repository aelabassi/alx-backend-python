#!/usr/bin/env python3
""" Async Comprehensions: measure_runtime """

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Coroutine that will execute async_comprehension
    four times in parallel
    using asyncio.gather.
    Then it will return the total runtime.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
