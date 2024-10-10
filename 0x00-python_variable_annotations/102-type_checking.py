#!/usr/bin/env python3
""" Check typing using mypy """

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Return a zoomed in list """
    zoomed_in: List = []
    for item in lst:
        for _ in range(factor):
            zoomed_in.append(item)
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
