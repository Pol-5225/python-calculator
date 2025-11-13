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