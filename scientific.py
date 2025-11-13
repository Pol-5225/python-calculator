import math

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of negative number"
    return math.sqrt(x)

def logarithm(x):
    if x <= 0:
        return "Error: Logarithm undefined for non-positive numbers"
    return math.log(x)

def factorial(x):
    if x < 0:
        return "Error: Factorial undefined for negative numbers"
    return math.factorial(int(x))

def sin_function(degrees):
    return math.sin(math.radians(degrees))

def cos_function(degrees):
    return math.cos(math.radians(degrees))

# Test scientific functions
if __name__ == "__main__":
    print("=== Scientific Functions Test ===")
    print(f"Square root of 16: {square_root(16)}")
    print(f"Log of 10: {logarithm(10)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Sin of 90 degrees: {sin_function(90)}")