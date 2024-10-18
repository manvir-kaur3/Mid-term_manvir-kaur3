#!/usr/bin/env python3

def calculate_factorial(n):
    """Return the factorial of the given positive integer n."""
    if n < 0:
        raise ValueError("Input must be a positive integer.")
    factorial = 1
    for i in range(1, n + 1):  
        factorial *= i          
    return factorial

if __name__ == '__main__':
    user_input = int(input("Enter a positive integer: "))  
    result = calculate_factorial(user_input)                
    print(f"The factorial of {user_input} is: {result}")    
