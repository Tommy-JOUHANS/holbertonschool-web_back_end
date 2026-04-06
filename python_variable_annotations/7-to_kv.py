#!/usr/bin/env python3
"""Module that contains a type-annotated function to_kv that takes
a string k and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v
and should be annotated as a float."""


from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """Return a tuple where the first element is the string k and the second
    element is the square of v as a float."""
    return (k, float(v ** 2))
