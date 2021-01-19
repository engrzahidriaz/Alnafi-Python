# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 06:31:58 2020

@author: Dell
"""


def extract_function_name(func): 
     def internal_method(*args, **kwargs): 
         print('The method called is:', func.__name__)
         returned_value = func(*args, **kwargs)
         print('The method execution is complete.')
         return returned_value 
     return internal_method
  
# # adding decorator to the function 
@extract_function_name
def sum_two_numbers(a, b): 
    print("This is called inside the function") 
    return a + b 

@extract_function_name
def product_two_numbers(a, b): 
    print("This is called inside the function") 
    return a*b 

a, b = 3, 4
# getting the value through return of the function 
print('Sum function value:', sum_two_numbers(a, b))
print('Product function value', product_two_numbers(a, b))