"""A simple command-line calculator."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "+": ("Add", add),
    "-": ("Subtract", subtract),
    "*": ("Multiply", multiply),
    "/": ("Divide", divide),
}


def run() -> None:
    print("Python Calculator")
    while True:
        print("\nChoose an operation: +  -  *  /  (or q to quit)")
        choice = input("> ").strip().lower()
        if choice == "q":
            print("Goodbye!")
            return
        if choice not in OPERATIONS:
            print("Please choose +, -, *, /, or q.")
            continue

        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
            label, operation = OPERATIONS[choice]
            result = operation(a, b)
            print(f"{label}: {a:g} {choice} {b:g} = {result:g}")
        except ValueError as error:
            print(f"Input error: {error}")


if __name__ == "__main__":
    run()
