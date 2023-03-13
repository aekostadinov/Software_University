from typing import List
from functools import reduce

class Calculator:

    @staticmethod
    def add(*nums: List[int]) -> int:
        return sum(nums)

    @staticmethod
    def multiply(*nums: List[int]) -> int:
        return reduce(lambda a, b: a * b, nums)

    @staticmethod
    def divide(*nums: List[int]) -> float:
        return reduce(lambda a, b: a / b, nums)

    @staticmethod
    def subtract(*nums: List[int]) -> int:
        return reduce(lambda a, b: a - b, nums)
