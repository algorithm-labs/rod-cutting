from rod_cutting.solvers.bottom_up import BottomUpRodCuttingSolver

from ..solver_test import SolverTest


class TestRecursiveTopTownRodCuttingSolver(SolverTest):
    Solver = BottomUpRodCuttingSolver