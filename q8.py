#!/usr/bin/env python3

def count_vowels(input_string):
    """Return the number of vowels in the given string."""
    vowels = "aeiouAEIOU"  
    count = 0
    
    for char in input_string:  
        if char in vowels:     
            count += 1         
    
    return count

if __name__ == '__main__':
    user_input = input("Enter a string: ")  
    result = count_vowels(user_input)        
    print(f"The number of vowels in '{user_input}' is: {result}")  
