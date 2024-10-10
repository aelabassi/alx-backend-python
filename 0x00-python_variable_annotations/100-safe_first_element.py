#!/usr/bin/env python3
""" Function that takes a Sequence of Anys and returns the first element
if the argument is not empty, otherwise None. """

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return first element of list if it is not empty, otherwise None """
    if lst:
        return lst[0]
    else:
        return None
