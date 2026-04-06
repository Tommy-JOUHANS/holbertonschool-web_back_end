#!/usr/bin/env python3
"""The types of the elements of the input are not known
but the types of the elements of the output are known."""


from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of the input sequence
if the sequence is not empty, otherwise return None."""
    if lst:
        return lst[0]
    else:
        return None
