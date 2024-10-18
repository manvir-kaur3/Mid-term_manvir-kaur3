#!/usr/bin/env python3

def calculate_factorial(n):
    """Return the factorial of the given positive integer n."""
    if n < 0:
        raise ValueError("Input must be a positive integer.")
    factorial = 1
    for i in range(1, n + 1):  # Loop from 1 to n
        factorial *= i          # Multiply each integer to get the factorial
    return factorial

if __name__ == '__main__':
    user_input = int(input("Enter a positive integer: "))  # Get input from the user
    result = calculate_factorial(user_input)                # Call the function
    print(f"The factorial of {user_input} is: {result}")    # Output the result
