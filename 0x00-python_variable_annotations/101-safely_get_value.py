#!/usr/bin/env python3
"""
Type-annotated function safely_get_value
"""

from typing import Mapping, Any, Union


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[Any, None] = None) \
        -> Union[Any, None]:
    """
    Function that returns the value of a key safely
    """
    if key in dct:
        return dct[key]
    else:
        return default
