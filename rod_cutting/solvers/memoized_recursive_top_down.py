from typing import List

import numpy as np

from rod_cutting.solver import RodCuttingSolver
from rod_cutting.instance import RodCuttingInstance
from rod_cutting.solution import RodCuttingSolution


class MemoizedRecursiveTopTown(RodCuttingSolver):
    '''
    Representation of a recursive top-down algorithm with memoization for solving the rod cutting problem.
    '''
    @classmethod
    def solve(cls, instance: RodCuttingInstance) -> RodCuttingSolution:
        '''
        Implementation of recursive top-down algorithm with memoization for solving the rod cutting problem.
        '''
        r = cls.initialize_cache(instance.rod_length)
        return cls._solve(instance, r)

    @classmethod
    def _solve(cls, instance: RodCuttingInstance, r: List[float]) -> RodCuttingSolution:
        '''
        Implementation of recursive top-down algorithm with memoization for solving the rod cutting problem.
        '''
        n = instance.rod_length
        if n == 0:
            return RodCuttingSolution(value=0.0)
        if r[n - 1] > -np.infty:
            return RodCuttingSolution(value=r[n - 1])
        p = instance.prices
        value = -np.infty
        for i in range(n):
            value = max(
                value, p[i] + cls.value( instance.restrict(n - i - 1), r )
            )
        r[n - 1] = value
        return RodCuttingSolution(value=value)

    @classmethod
    def value(cls, instance: RodCuttingInstance, r: List[float] = None) -> float:
        r = cls.initialize_cache(instance.rod_length) if r is None else r
        return cls._solve(instance, r).value

    @classmethod
    def initialize_cache(cls, n: int) -> List[float]:
        return [-np.infty for _ in range(n)]


MemoizedRecursiveTopTownRodCuttingSolver = MemoizedRecursiveTopTown
