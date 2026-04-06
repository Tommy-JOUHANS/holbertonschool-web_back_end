#!/usr/bin/env python3
"""Module that contains a type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function that multiplies
a float by multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiplier_func(n: float) -> float:
        """Return the product of n and multiplier as a float."""
        return n * multiplier
    return multiplier_func
