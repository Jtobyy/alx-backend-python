#!/usr/bin/env python3
"""
Complex types - funtions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
