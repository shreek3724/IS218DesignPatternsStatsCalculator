"""Store two operands and a callable; run math only in get_result."""
from math import isfinite
from calculator.validation import numeric_values


class Calculation:

    #the constructor is this section right below:
    def __init__(self, values, operation):
        numbers = numeric_values(values)
        self.a = numbers[0]
        self.b = numbers[1]
        self.operation = operation

    def get_result(self):
        result = float(self.operation(self.a, self.b))
        if not isfinite(result):
            raise ValueError("Result is outside the supported range.")
            # this is the new part we are adding- it ensures all inputs are valid prior to calculation
        return result