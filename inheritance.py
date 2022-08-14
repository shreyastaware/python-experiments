#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 21:29:03 2022

@author: shreyastaware
"""

# Python code to demonstrate how parent constructors
# are called.

# =============================================================================
# Types of Inheritance – 
# Single Inheritance:
# Single-level inheritance enables a derived class to inherit characteristics
#  from a single-parent class.

# Multilevel Inheritance:
# Multi-level inheritance enables a derived class to inherit properties from
#  an immediate parent class which in turn inherits properties from his parent
#  class.

# Hierarchical Inheritance:
# Hierarchical level inheritance enables more than one derived class to
#  inherit properties from a parent class.

# Multiple Inheritance:
# Multiple level inheritance enables one derived class to inherit properties
#  from more than one base class.
# =============================================================================

# parent class
class Person(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
	
# child class
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
		print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()
