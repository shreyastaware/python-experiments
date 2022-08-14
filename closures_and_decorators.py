#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 20:43:06 2022

@author: shreyastaware
"""

# =============================================================================
# Conditions for being a closure

# - We must have a nested function (function inside a function).
# - The nested function must refer to a value defined in the enclosing function.
# - The enclosing function must return the nested function.

# Why we need closures?

# Closures can avoid the use of global values and provides some form of data
 # hiding.

# This technique by which some data (`Hello` in this case) gets
#  attached to the code is called **closure in Python**.

# This value in the enclosing scope is remembered even when the variable goes
#  out of scope or the function itself is removed from the current namespace.

# =============================================================================

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")
    
pretty = make_pretty(ordinary)
# pretty is a closure

def make_handsome(func):
    def inside():
        print("Showing how a decorator is used")
        func()
    return inside

@make_handsome # adding a decorator
def normal():
    print("I am normal")

handsome = normal
# handsome is a closure

# calling pretty and handsome
pretty()
handsome()

print(pretty.__closure__, handsome.__closure__)
print(pretty.__closure__[0].cell_contents, 
      handsome.__closure__[0].cell_contents)

