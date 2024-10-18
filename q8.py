#!/usr/bin/env python3

def count_vowels(input_string):
    """Return the number of vowels in the given string."""
    vowels = "aeiouAEIOU"  # Define vowels (both lowercase and uppercase)
    count = 0
    
    for char in input_string:  # Loop through each character in the string
        if char in vowels:     # Check if the character is a vowel
            count += 1         # Increment the count
    
    return count

if __name__ == '__main__':
    user_input = input("Enter a string: ")  # Get input from the user
    result = count_vowels(user_input)        # Call the function
    print(f"The number of vowels in '{user_input}' is: {result}")  # Output the result
