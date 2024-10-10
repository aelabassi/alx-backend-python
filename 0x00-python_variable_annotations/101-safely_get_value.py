#!/usr/bin/env python3
"""
Type-annotated function safely_get_value
"""

from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) \
        -> Union[T, None]:
    """
    Function that returns the value of a key safely
    """
    if key in dct:
        return dct[key]
    else:
        return default
