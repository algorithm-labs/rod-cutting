from rod_cutting.instance import RodCuttingInstance
from rod_cutting.solution import RodCuttingSolution


# Cormen, Leiserson, Rivest, Stein: Introduction to Algorithms, 3rd Edition
# Chaper 15, Section 15.1
CLRS_15_1 = RodCuttingInstance(
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
)
CLRS_15_1_OPTIMAL_REVENUES = [1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
# Restrict CLRS_15_1 to rod size 4
CLRS_15_1_4 = CLRS_15_1.restrict_to_rod_size(4)
CLRS_15_1_4_SOLUTION = RodCuttingSolution(value=10)