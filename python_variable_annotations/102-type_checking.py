#!/usr/bin/env python3
"""Module that contains the following piece of code and
apply any necessary changes."""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list that contains the same elements as lst but
    with each element repeated factor times."""
    zoomed = []
    for i in lst:
        zoomed.extend([i] * factor)
    return zoomed
