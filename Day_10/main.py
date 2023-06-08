# CALCULATOR PROGRAM
from art import logo


# ADD
def add(n1, n2):
    return n1 + n2


# SUBTRACT
def subtract(n1, n2):
    return n1 - n2


# MULTIPLY
def multiply(n1, n2):
    return n1 * n2


# DIVIDE
def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def print_operators():
    for key in operators:
        print(key)


def calculator():
    def execute_operation():
        num1 = int(input("What's the first number?: "))
        print_operators()
        operation_key = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        operation = operators[operation_key]
        answer = operation(num1, num2)
        print(f"{num1} {operation_key} {num2} = {answer}")
        return answer

    def another_operation(previous_answer):
        next_operation_key = input("Pick an operation from the lines above: ")
        num3 = int(input("What's the next number?: "))
        chosen_operation_fn = operators[next_operation_key]
        new_answer = chosen_operation_fn(previous_answer, num3)
        print(f"{previous_answer} {next_operation_key} {num3} = {new_answer}")
        return new_answer

    first_answer = execute_operation()

    should_continue = True

    while should_continue:

        another = input(f"Type 'y' to perform another operation with {first_answer}, Type 'r' to start fresh: Type "
                        f"'n' to exit ").lower()

        if another == 'y':
            last_answer = another_operation(first_answer)
            first_answer = last_answer
        elif another == 'r':
            should_continue = False
            calculator()
        else:
            should_continue = False


print(logo)
calculator()
