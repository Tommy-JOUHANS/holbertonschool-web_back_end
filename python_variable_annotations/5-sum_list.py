#!/usr/bin/env python3
"""Module that contains a type-annotated function sum_list which
takes a list input_l of floats as argument and returns
their sum as a float."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of the floats in input_list as a float."""
    return sum(input_list)
