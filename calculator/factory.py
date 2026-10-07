from calculator.calculation import Calculation
from calculator.operations import Operations

# created in part 2 

# this factory translates the english to know what calculation to do, and what operation to pull
# so the factory is creating the route to the command that needs to run!
# factory creates the calculations

# it translates the english
# gives the worker the correct machiene


# the registry is a class attribute!

# part 2, added multiply and divide to the registry! 
# also added abs_diff as a part of part 2 independent task
class CalculationFactory:
    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
        "abs_diff": Operations.abs_diff,
    }
    # this is the translation dictionary
    # doing Operations.add(#,#) would have it immediatley do the calculation
    # doing Operations.add NO PARENTHESES would just store the behaviour

    @staticmethod
    def create(name, a, b):
        name = name.strip().lower()
        try:
            operation = CalculationFactory.operations[name]
        except KeyError:
            raise ValueError(f"Unknown operation: {name}") from None
        return Calculation(a, b, operation) # WHERE THE FACTORY ACTUALLY CREATES THE CALCULATION
    # allows us to do CalculationFactory.create("add", 2, 3)
    # without doing factory = CalculationFactory()


'''

def create_add(a, b):
    return Calculation([a, b], Operations.add)


"""A factory centralizes construction; it does not execute math."""
from calculator.calculation import Calculation
from calculator.operations import Operations


calculation = create_add(2, 3)

print(type(calculation))
print(calculation.get_result())
'''
