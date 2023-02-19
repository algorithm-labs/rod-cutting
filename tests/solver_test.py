from typing import Type

from rod_cutting.solution import RodCuttingSolution
from rod_cutting.solver import RodCuttingSolver
from rod_cutting.solvers.recursive_top_down import RecursiveTopTownRodCuttingSolver

from .instances import (
    CLRS_15_1,
    CLRS_15_1_4, 
    CLRS_15_1_4_SOLUTION,
    CLRS_15_1_OPTIMAL_REVENUES,
)


class SolverTest():
    Solver: Type[RodCuttingSolver]

    def test_instantiation(self):
        solver = self.Solver()
        assert isinstance(solver, RodCuttingSolver)


    def test_solve_clrs_15_1_4(self):
        solver = self.Solver()
        solution = solver.solve(CLRS_15_1_4)
        assert isinstance(solution, RodCuttingSolution)
        assert solution.value == CLRS_15_1_4_SOLUTION.value


    def test_call_clrs_15_1_4(self):
        solver = self.Solver()
        solution = solver(CLRS_15_1_4)
        assert isinstance(solution, RodCuttingSolution)
        assert solution.value == CLRS_15_1_4_SOLUTION.value


    def test_solve_as_classmethod_clrs_15_1_4(self):
        solution = self.Solver.solve(CLRS_15_1_4)
        assert isinstance(solution, RodCuttingSolution)
        assert solution.value == CLRS_15_1_4_SOLUTION.value


    def test_solve_all_clrs_15_1(self, subtests):
        for n in range(1, 11):
            with subtests.test(msg=f"Testing CLRS_15_1 with rod size {n}", i=n):
                instance = CLRS_15_1.restrict(n)
                solution = self.Solver.solve(instance)
                assert solution.value == CLRS_15_1_OPTIMAL_REVENUES[n-1]