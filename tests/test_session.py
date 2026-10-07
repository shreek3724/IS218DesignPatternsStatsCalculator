import pytest
from calculator.calculation import Calculation
from calculator.operations import Operations
from calculator.session import CalculatorSession

# added during part 3, session and reciever part

def test_successful_calculation_recorded():
    session = CalculatorSession()
    calculation = Calculation([3, 9], Operations.abs_diff)
    result = session.calculate(calculation)
    assert result == 6
    assert session.get_history() == [(calculation, 6)]

def test_failed_calculation_not_recorded():
    session = CalculatorSession()
    calculation = Calculation([3, 0], Operations.divide)

    with pytest.raises(ZeroDivisionError):
        session.calculate(calculation)

    assert session.get_history() == []

def test_clear_removes_history():
    session = CalculatorSession()
    calculation = Calculation([3, 9], Operations.abs_diff)

    session.calculate(calculation)

    assert session.get_history() == [(calculation, 6)]

    session.clear()

    assert session.get_history() == []

def test_sessions_have_independent_histories():
    # Arrange
    session_one = CalculatorSession()
    session_two = CalculatorSession()

    calculation = Calculation([3, 9], Operations.abs_diff)

    # Act
    session_one.calculate(calculation)

    # Assert
    assert session_one.get_history() == [(calculation, 6)]
    assert session_two.get_history() == []
    
def test_mutating_returned_history_does_not_change_internal_history():
    session = CalculatorSession()
    calculation = Calculation([3, 9], Operations.abs_diff)

    session.calculate(calculation)

    returned_history = session.get_history()
    returned_history.clear()

    assert session.get_history() == [(calculation, 6)]

# added during part 4 to test count command
def test_count_only_includes_successful_calculations():
    session = CalculatorSession()

    successful = Calculation([3, 9], Operations.abs_diff)
    failed = Calculation([3, 0], Operations.divide)

    session.calculate(successful)

    with pytest.raises(ZeroDivisionError):
        session.calculate(failed)

    assert session.count() == 1