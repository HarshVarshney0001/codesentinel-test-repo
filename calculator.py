def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    # BUG: no check for b == 0
    return a / b

def average(numbers):
    # BUG: empty list will cause divide by zero
    total = sum(numbers)
    return total / len(numbers)

def multiply(a, b):
    return a * b
