# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 06:21:00 2020

@author: Dell
"""


import pdb

def sum_values(a, b):
    return a + b

def test_function1():
    pdb.set_trace()  #we have added a breakpoint here. The code pause execution here.
    print('This is the first line')
    print("This is the second line.")
    value  = sum_values(2, 3)
    print('The code is done!')
    return value 


test_function1()

def sub_values(a, b):
    return a - b

def test_function2():
    pdb.set_trace()  #we have added a breakpoint here. The code pause execution here.
    print('This is the first line')
    print("This is the second line.")
    value  = sub_values(3, 2)
    print('The code is done!')
    return value 


test_function2()



def multi_values(a, b):
    return a * b

def test_function3():
    pdb.set_trace()  #we have added a breakpoint here. The code pause execution here.
    print('This is the first line')
    print("This is the second line.")
    value  = multi_values(2, 3)
    print('The code is done!')
    return value 


test_function3()


def divid_values(a, b):
    return a / b

def test_function4():
    pdb.set_trace()  #we have added a breakpoint here. The code pause execution here.
    print('This is the first line')
    print("This is the second line.")
    value  = divid_values(3, 2)
    print('The code is done!')
    return value 


test_function4()