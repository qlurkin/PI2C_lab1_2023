import pytest
import utils
import math

def test_fact():
    assert utils.fact(0) == 1
    assert utils.fact(4) == 24
    with pytest.raises(ValueError):
        utils.fact(-1)

def test_roots():
    assert isinstance(utils.roots(2, 0, 0), tuple)
    assert utils.roots(2, 0, 0) == pytest.approx((0.0,))
    assert utils.roots(2, 0, -2) == pytest.approx((-1.0, 1.0))
    assert utils.roots(2, 1, -2) == pytest.approx((-1.28077640, 0.78077640))
    assert utils.roots(2, 1, 2) == tuple()

def test_integrate():
    assert abs(utils.integrate('(1 - x**2) ** (1/2)', -1, 1) - math.pi/2) < 0.00001
    assert utils.integrate('(1 - x**2) ** (1/2)', -1, 1) == pytest.approx(math.pi/2)
