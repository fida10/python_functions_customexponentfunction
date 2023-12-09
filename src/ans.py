""" 
Practice Question 2: Custom Exponent Function

Task:

Create a function custom_exponent that takes two numbers, a base and an exponent, and returns the base raised to the specified exponent without using the ** operator or pow() function.
"""

def custom_exponent(base, exp):
    ans = 1
    for i in range(0, exp):
        ans *= base
    
    return ans