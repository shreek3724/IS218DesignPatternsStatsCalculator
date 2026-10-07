"""CLI prepares requests, invokes commands, and recovers from expected failures."""
from calculator.factory import CalculationFactory
from calculator.session import CalculatorSession
from calculator.commands import CalculateCommand, ClearHistoryCommand, CountCommand, HelpCommand, HistoryCommand

# added as part of part 4

def prepare_command(text, session):
    #the boundary between text input and our object-oriented system.

    parts = text.split()
    if not parts:
        raise ValueError("Enter a command; use help for examples.")
    name, *arguments = parts
    name = name.lower()

    # added count (during part 4) to actions options! 
    actions = {
    "history": HistoryCommand,
    "clear": ClearHistoryCommand,
    "count": CountCommand,
}
    
    if name in actions:
        if arguments:
            raise ValueError(f"{name} does not accept values.")
        return actions[name](session)
    if name == "help":
        if arguments:
            raise ValueError("help does not accept values.")
        return HelpCommand()
    values = []
    options = {}
    for argument in arguments:
        if "=" in argument:
            key, value = argument.split("=", 1)
            if not key or key in options:
                raise ValueError("Options need unique names: key=value.")
            options[key] = value
        else:
            values.append(argument)
    arguments = values
    calculation = CalculationFactory.create(name, *arguments, **options)
    return CalculateCommand(session, calculation)


def run() -> None:
    # The REPL loop!
    # Read → Evaluate → Print → Loop
    session = CalculatorSession()
    print("Calculator")
    print(HelpCommand().execute())
    while True:
        try:
            text = input("> ").strip()
            if text.lower() == "exit":
                break

            command = prepare_command(text, session)
            print(command.execute())
            # super key lines!
            # the entire Command pattern in action.
            # it says, "Figure out what action this text represents."
            # then do execute() bc polymorphism allows it to use the common contract, and not have to specify

        except (EOFError, KeyboardInterrupt):
            print()
            break
        except (ValueError, OSError, ZeroDivisionError, OverflowError) as error:
            print(f"Error: {error}")
            # error recovery 
            # ensures the while loop continues even if an error is caught
    print("Goodbye!")