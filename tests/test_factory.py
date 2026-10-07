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

# part 3 tests, test square, sqrt, sum, wrong operand counts, and delayed domain errors. A negative real square root fails during execution.
def test_factory_creates_square():
    calculation = CalculationFactory.create("square", 5)

    assert calculation.get_result() == 25

def test_factory_rejects_wrong_square_operand_count():
    with pytest.raises(ValueError, match="square requires exactly 1"):
        CalculationFactory.create("square", 5, 2)

def test_factory_creates_sqrt():
    calculation = CalculationFactory.create("sqrt", 9)

    assert calculation.get_result() == 3

def test_factory_rejects_wrong_sqrt_operand_count():
    with pytest.raises(ValueError, match="sqrt requires exactly 1"):
        CalculationFactory.create("sqrt", 9, 3)

def test_factory_creates_sum():
    calculation = CalculationFactory.create("sum", 1, 2, 3, 4)

    assert calculation.get_result() == 10

def test_sum_requires_at_least_one_value():
    calculation = CalculationFactory.create("sum")

    with pytest.raises(ValueError, match="at least one"):
        calculation.get_result()

def test_sqrt_domain_error_is_deferred_until_execution():
    calculation = CalculationFactory.create("sqrt", -1)

    with pytest.raises(ValueError):
        calculation.get_result()

# part 3 test for power operation, and * and **
def test_factory_power_with_exponent():
    calculation = CalculationFactory.create("power", 3, exponent=4)
    assert calculation.get_result() == 81

# part 3 tests for divide_by_factor
def test_divide_by_factor():
    calculation = CalculationFactory.create("divide_by_factor", 10, factor=2)
    assert calculation.get_result() == 5

def test_divide_by_factor_rejects_unsupported_option():
    with pytest.raises(ValueError, match="Unsupported option"):
        CalculationFactory.create("divide_by_factor", 10, banana=5)

def test_divide_by_factor_zero_factor_fails_during_execution():
    calculation = CalculationFactory.create(
        "divide_by_factor",
        10,
        factor=0
    )

    with pytest.raises(ZeroDivisionError):
        calculation.get_result()