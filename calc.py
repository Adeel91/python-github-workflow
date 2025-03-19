def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Returns the division of two numbers. Handles division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    print("Sum:", add(3, 2))
    print("Difference:", subtract(3, 2))
    print("Product:", multiply(3, 2))
    print("Quotient:", divide(3, 2))
