import numpy as np

from rod_cutting.solver import RodCuttingSolver
from rod_cutting.instance import RodCuttingInstance
from rod_cutting.solution import RodCuttingSolution


class BottomUp(RodCuttingSolver):
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
        r = [0.0] + [-np.infty for _ in range(n)]
        for j in range(1, n+1):
            value = -np.infty
            for i in range(j): 
                value = max( value, p[i] + r[j-i-1] )
            r[j] = value
        return RodCuttingSolution(value=value)

    @classmethod
    def value(cls, instance: RodCuttingInstance) -> float:
        return cls.solve(instance).value


BottomUpRodCuttingSolver = BottomUp
