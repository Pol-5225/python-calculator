# Simple Calculator v1.0
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Test the functions
if __name__ == "__main__":
    print("Calculator Started!")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")

  # Adding new function for the ability of multiplication.
    def multiply(a, b):
        return a * b

    # Add to your test section:
    print(f"4 * 3 = {multiply(4, 3)}")

# Adding new a function for ability to divide
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b


    # Test it:
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"5 / 0 = {divide(5, 0)}")
# Just a simple comment to see GIT revert commit option how it works