#!/usr/bin/env python3
""" 4 - Tasks """

import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns list of delays in ascending order
     Args:
         n: int - number of delays
         max_delay: int - max delay
     Returns:
         List[float]: list of delays in ascending order
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
