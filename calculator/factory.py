from calculator.calculation import Calculation
from calculator.operations import Operations
from calculator.validation import numeric_values

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
        "square": Operations.square,
        "sqrt": Operations.sqrt,
        "sum": Operations.sum,
        "power": Operations.power,
        "divide_by_factor": Operations.divide_by_factor,
        "mean": Operations.mean,
        "stddev": Operations.stddev,
    }
    # this is the translation dictionary
    # doing Operations.add(#,#) would have it immediatley do the calculation
    # doing Operations.add NO PARENTHESES would just store the behaviour

    #added during part 3, to define how many inputs each needs, except sum bc it can take any amt
    operand_counts = {
    "add": 2, "subtract": 2, "multiply": 2, "divide": 2,
    "square": 1, "sqrt": 1, "power": 1, "divide_by_factor": 1,
}
    # added in part 3 to allow exponent as a named option
    allowed_options = {
    "power": {"exponent"},
    "divide_by_factor": {"factor"},
    "stddev": {"ddof"},
    # allows the user to input power as one of the options 
    # like: CalculationFactory.create("power", 3, exponent=4)
}

# part 3 - new create method that also checks operand counts

    @staticmethod
    def create(name, *values, **options):
        name = name.strip().lower()
        try:
            operation = CalculationFactory.operations[name]
        except KeyError:
            raise ValueError(f"Unknown operation: {name}") from None

        count = CalculationFactory.operand_counts.get(name)

        # added in part 3
        # checks that the option the user picks is allowed in our registry!
        # ex. they can only pick exponent=# rn!
        allowed = CalculationFactory.allowed_options.get(name, set())
        converted_options = {}
        for key, value in options.items():
            if key not in allowed:
                raise ValueError(f"Unsupported option for {name}: {key}")
            converted_options[key] = numeric_values([value])[0]

        #count = CalculationFactory.operand_counts.get(name)
        if count is not None and len(values) != count:
            raise ValueError(f"{name} requires exactly {count} value(s).")
        return Calculation(values, operation, **converted_options)

'''
 @staticmethod
    def create(name, *values):
        name = name.strip().lower()
        try:
            operation = CalculationFactory.operations[name]
        except KeyError:
            raise ValueError(f"Unknown operation: {name}") from None
        return Calculation(values, operation) # WHERE THE FACTORY ACTUALLY CREATES THE CALCULATION
    # allows us to do CalculationFactory.create("add", 2, 3)
    # without doing factory = CalculationFactory()
'''

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
