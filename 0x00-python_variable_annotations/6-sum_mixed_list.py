#!/usr/bin/env python3
"""
Complex types - mixed list
"""
from typing import List, Union
from functools import reduce


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Returns the sum of the elements in the mxd_list as a float"""
    return float(reduce(lambda x, y: x + y, mxd_list))
