import pytest
from calculator.calculation import Calculation
from calculator.operations import Operations


def test_construction_defers_execution():
    calls = []

    def operation(a, b):
        calls.append((a, b))
        return a + b

    calculation = Calculation(2, 3, operation)

    assert calls == []
    assert calculation.get_result() == 5
    assert calls == [(2, 3)]


def test_zero_division_occurs_during_execution():
    calculation = Calculation(1, 0, Operations.divide)

    with pytest.raises(ZeroDivisionError):
        calculation.get_result()


def test_reject_nonfinite_result():
    with pytest.raises(ValueError, match='range'):
        Calculation(1e+308, 1e+308, Operations.multiply).get_result()


"""
adding in work for: "fill in get_result for a stored subtract callable before looking at the reference."
MEANS: "Prove that the Calculation class can store Operations.subtract and execute it later."

and work for independent and completion tasks
"""


def test_stored_subtract_operation():
    calculation = Calculation(10, 4, Operations.subtract)

    assert calculation.get_result() == 6


def test_stored_abs_diff_operation():
    calculation = Calculation(3, 9, Operations.abs_diff)

    assert calculation.get_result() == 6