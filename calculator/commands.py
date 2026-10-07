# added during part 4
from abc import ABC, abstractmethod
# from unittest import result
HELP = "Commands: add/subtract/multiply/divide A B; square/sqrt VALUE; power VALUE exponent=N; sum VALUES; history; clear; help; exit"

class Command(ABC):
    # abstraction! 
    # means Any concrete subclass of Command must provide its own execute() implementation.
    @abstractmethod
    def execute(self) -> str:
        """Perform an action and return display text; expected errors may propagate."""

class CalculateCommand(Command):
    def __init__(self, session, calculation):
        self.session = session
        self.calculation = calculation
    # the constructor of an OBJECT
    # "Here is the Session that should do the work
    # and here is the Calculation I want it to perform. Keep them for later."

    def execute(self) -> str:
        result = self.session.calculate(self.calculation)
        return f"Result: {result:.4f}"
    # does the work!


class ClearHistoryCommand(Command):
    def __init__(self, session):
        self.session = session

    def execute(self) -> str:
        self.session.clear()
        return "History cleared."

# adding a HistoryCommand - to view past history! 
# and a Help command! 

class HistoryCommand(Command):
    # Ask the CalculatorSession for its saved history and turn that into text.
    '''
    def __init__(self, session):
            self.session = session
    
        def execute(self):
            entries = self.session.get_history() # gets the saved entries 
            if not entries:
                return "No history."
            return "\n".join(
                f"{calculation.get_result():.4f}" for calculation, _ in entries
            )
    '''

    def __init__(self, session):
        self.session = session

    def execute(self) -> str:
        lines = []
        for calculation, result in self.session.get_history():
            values = " ".join(str(value) for value in calculation.values)
            options = " ".join(f"{key}={value}" for key, value in calculation.options.items())
            request = " ".join(part for part in (calculation.operation.__name__, values, options) if part)
            lines.append(f"{request} = {result:.4f}")
        return "\n".join(lines) or "History is empty."

class CountCommand(Command):
    # added as a part of part 4 work
    def __init__(self, session):
        self.session = session

    def execute(self) -> str:
        return f"Count: {self.session.count()}"

class HelpCommand(Command):
    # doesnt need a session bc doesnt ask the session to do anything! 
    def execute(self) -> str:
        return HELP
    '''
    def execute(self):
            return (
                "Commands:\n"
                "  add <a> <b>\n"
                "  subtract <a> <b>\n"
                "  multiply <a> <b>\n"
                "  divide <a> <b>\n"
                "  history\n"
                "  clear\n"
                "  help"
            )
    '''

'''
class IncompleteCommand(Command):
    def execute(self) -> str:
        return "Done"
IncompleteCommand()
# proved that it needs execut() to instantiate
'''
