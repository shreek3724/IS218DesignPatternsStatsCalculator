import pytest
from calculator.calculation import Calculation
from calculator.operations import Operations
from calculator.history import History
# from calculator.session import CalculatorSession


def test_history_copy_protects_collection_membership():
    # a test that ensures History class protects its internal list
    history = History() # we create an object of class History to be an empty record book! 
    calculation = Calculation(2, 3, Operations.add)
    
    history.add(calculation, 5.0) # we store the test calculation and its result
    snapshot = history.get_history() # we see the copy of the real recordbook
    snapshot.clear() # we erase everything from our copy, but maintain the original copy! 
    assert history.get_history() == [(calculation, 5.0)]


def test_history_objects_are_shared_by_the_shallow_copy():
    history = History()
    calculation = Calculation(2, 3, Operations.add)
    history.add(calculation, 5.0)
    snapshot = history.get_history()
    assert snapshot[0][0] is calculation


def test_history_rejects_non_calculations():
    with pytest.raises(TypeError):
        History().add("add 2 3", 5)
    # controls what is allowed into internal records 

'''
def test_sessions_have_independent_history():
    first, second = CalculatorSession(), CalculatorSession()
    first.calculate(Calculation([2, 3], Operations.add))
    assert second.get_history() == []
    first.clear()
    assert first.get_history() == []
'''
