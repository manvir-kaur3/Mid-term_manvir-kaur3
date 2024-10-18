#!/usr/bin/env python3

def reverse_string(input_string):
    reversed_str = ""  
    for char in input_string:   
        reversed_str = char + reversed_str  
    return reversed_str

if __name__ == '__main__':
    user_input = input("Enter a string: ")  
    result = reverse_string(user_input)  
    print(f"The reversed string is: {result}")  
