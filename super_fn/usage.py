#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 00:06:19 2022

@author: shreyastaware
"""

# =============================================================================
# Python super()
# The Python super() function returns objects represented in the parent’s class
#  and enables multiple inheritances.

# Understanding Python super() with __init__() methods
# Python has a reserved method called “__init__.” In Object-Oriented language,
#  it is referred to as a constructor. When this method is called it allows the
#  class to initialize the attributes of the class. In an inherited subclass, a
#  parent class can be referred to with the use of the super() function. The
#  super function returns a temporary object of the superclass that allows
#  access to all of its methods to its child class.

# The benefits of using a superclass are:
# Need not remember or specify the parent class name to access its methods.
#  This function can be used both in single and multiple inheritances.
# This implements modularity (isolating changes) and code reusability as there
#  is no need to rewrite the entire function.
# Super function in Python is called dynamically because Python is a dynamic
#  language, unlike other languages.
# There are 3 constraints to using the super function:- 

# The class and its methods which are referred to by the super function
# The arguments of the super function and the called function should match.
# Every occurrence of the method must include super() after you use it.
# =============================================================================

class Emp():
	def __init__(self, id, name, Add):
		self.id = id
		self.name = name
		self.Add = Add

# Class freelancer inherits EMP
class Freelance(Emp):
	def __init__(self, id, name, Add, Emails):
		super().__init__(id, name, Add)
		self.Emails = Emails

Emp_1 = Freelance(103, "Suraj kr gupta", "Noida" , "KKK@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)

