import pytest
import itertools

from rod_cutting.solvers import (
    BottomUpRodCuttingSolver,
    MemoizedRecursiveTopTownRodCuttingSolver,
    RecursiveTopTownRodCuttingSolver,
)

from ..instances import CLRS_15_1

ROD_SIZES = range(1, CLRS_15_1.n + 1)
SOLVERS = [
    BottomUpRodCuttingSolver,
    MemoizedRecursiveTopTownRodCuttingSolver,
    RecursiveTopTownRodCuttingSolver,
]
BENCHMARKS = itertools.product(ROD_SIZES, SOLVERS)


@pytest.mark.parametrize("rod_size, Solver", BENCHMARKS)
def benchmark_bottom_up_clrs_15_1(benchmark, rod_size, Solver):
    instance = CLRS_15_1.restrict(rod_size)
    benchmark(Solver.solve, instance)