from abc import ABC, abstractmethod

from pydantic import BaseModel

from rod_cutting.instance import RodCuttingInstance
from rod_cutting.solution import RodCuttingSolution


class RodCuttingSolver(BaseModel, ABC):
    @abstractmethod
    def solve(instance: RodCuttingInstance) -> RodCuttingSolution:
        '''
        Method to solve instances of rod cutting.
        '''
        
    def value(self, instance: RodCuttingInstance) -> float:
        return self.solve(instance).value

    def __call__(self, instance: RodCuttingInstance) -> RodCuttingSolution:
        return self.solve(instance)
