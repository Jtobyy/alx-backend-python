#!/usr/bin/env python3
"""
Complex types - list of floats
"""
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    """ Returns the sum of the elements in input_list """
    return reduce(lambda x, y: x + y, input_list)
