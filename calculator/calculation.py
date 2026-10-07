"""Store two operands and a callable; run math only in get_result."""
from math import isfinite
from calculator.validation import numeric_values

# new updated version as part of part 3
# allows for flexible inputs 

class Calculation:
    def __init__(self, values, operation, **options):
        self.values = numeric_values(values)
        self.operation = operation
        self.options = dict(options)

    def get_result(self) -> float:
        result = float(self.operation(*self.values, **self.options))
        # *self.values unpacks the list of values into individual arguments for the operation to use!
        if not isfinite(result):
            raise ValueError("Result is outside the supported range.")
        return result

'''
# updated calculation code in part 2 to match up with the factory

class Calculation:
    def __init__(self, a, b, operation):
        # creates a calculation with two operands and an operation
        # inside object called CALCULATION
        numbers = numeric_values([a, b])
        self.a = numbers[0]
        self.b = numbers[1]
        self.operation = operation

    def get_result(self):
        result = float(self.operation(self.a, self.b))
        if not isfinite(result):
            raise ValueError("Result is outside the supported range.")
        return result

'''

'''
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

'''