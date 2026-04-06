#!/usr/bin/env python3
"""Module that contains Annotate the below function's parameters
and return values with the appropriate types"""

from typing import Tuple, List, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples where the first element of the tuple is the
    sequence and the second element is the length of the sequence."""
    return [(i, len(i)) for i in lst]
