#!/usr/bin/env python3
"""Type-annotated function element_length
 that takes a iterable list as argument
and returns the length of the list"""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Type-annotated function element_length
    that takes a iterable list as argument
    and returns the length of the list"""
    return [(i, len(i)) for i in lst]
