#!/usr/bin/env python3
""" Concurrency with async coroutines """

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns list of delays in ascending order
     Args:
         n: int - number of delays
         max_delay: int - max delay
     Returns:
         List[float]: list of delays in ascending order
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
