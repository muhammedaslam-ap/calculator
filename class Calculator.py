class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b

    def subtract(self, a, b):
        self.result = a - b

    def multiply(self, a, b):
        self.result = a * b

    def divide(self, a, b):
        if b != 0:
            self.result = a / b
        else:
            raise ValueError("Cannot divide by zero.")

    def get_result(self):
        return self.result

# Create a new calculator object.
calculator = Calculator()

# Add two numbers together.
calculator.multiply(45, 45)

# Get the result.
result = calculator.get_result()

# Print the result.
print(result)