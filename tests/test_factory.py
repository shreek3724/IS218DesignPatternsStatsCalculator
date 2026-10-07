import pytest
from calculator.factory import CalculationFactory
# bc factory is the thing we are testing

def test_factory_rejects_unknown_operation():
    with pytest.raises(ValueError, match="Unknown operation"):
        CalculationFactory.create("banana", 2, 3)

def test_factory_defers_zero_division():
    calculation = CalculationFactory.create("divide", 1, 0)

    with pytest.raises(ZeroDivisionError):
        calculation.get_result()

def test_factory_does_not_execute_operation_during_creation():
    calls = []

    # spy tells us if the function is called!
    def spy(a, b):
        calls.append((a, b))
        return a + b
    # writes down the numbers if someone uses this (add) operation

    original = CalculationFactory.operations["add"]
    # saves the real operation so that we can put it back 
    CalculationFactory.operations["add"] = spy
    # replace add in the dictionary with our spy, and then create the calculation
    # lets us know if add was executed 

    calculation = CalculationFactory.create("add", 2, 3)

    assert calls == []

    CalculationFactory.operations["add"] = original

# added for part 2 indepdent task

# name normalization test
def test_factory_normalizes_operation_name():
    calculation = CalculationFactory.create(" ABS_DIFF ", 3, 9)

    assert calculation.get_result() == 6

# unknown abs_diff name test
def test_factory_rejects_unknown_abs_diff_name():
    with pytest.raises(ValueError, match="Unknown operation"):
        CalculationFactory.create("abs_difference", 3, 9)

# added as part of part 2 to test if the factory works for multiply and abs_diff 
def test_factory_creates_multiply():
    calculation = CalculationFactory.create("multiply", 2, 3)

    assert calculation.get_result() == 6

def test_factory_creates_abs_diff():
    calculation = CalculationFactory.create("abs_diff", 3, 9)

    assert calculation.get_result() == 6