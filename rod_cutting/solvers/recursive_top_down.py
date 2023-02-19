import numpy as np

from rod_cutting.solver import RodCuttingSolver
from rod_cutting.instance import RodCuttingInstance
from rod_cutting.solution import RodCuttingSolution


class RecursiveTopTown(RodCuttingSolver):
    '''
    Representation of a recursive top-down algorithm for solving the rod cutting problem.
    '''
    @classmethod
    def solve(cls, instance: RodCuttingInstance) -> RodCuttingSolution:
        '''
        Implementation of recursive top-down algorithm for solving the rod cutting problem.
        '''
        n = instance.rod_length
        p = instance.prices
        if n == 0:
            return RodCuttingSolution(value=0.0)
        value = -np.infty
        for i in range(n):
            value = max(
                value, p[i] + cls.value( instance.restrict(n - i - 1) )
            )
        return RodCuttingSolution(value=value)

    @classmethod
    def value(cls, instance: RodCuttingInstance) -> float:
        return cls.solve(instance).value


RecursiveTopTownRodCuttingSolver = RecursiveTopTown
