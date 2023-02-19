import pytest

from pydantic import ValidationError

from rod_cutting.instance import RodCuttingInstance


def test_instance():
    prices = [2.1, 3, 4.5]
    instance = RodCuttingInstance(prices=prices)
    assert instance.rod_length == len(prices)
    assert instance.n == instance.rod_length
    assert instance.prices == prices

def test_instance_price_constraints():
    prices = [2.1, -3, 4.5]
    with pytest.raises(ValidationError):
        RodCuttingInstance(prices=prices)