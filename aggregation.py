#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 23:06:12 2022

@author: shreyastaware
"""

# Use Aggregation > Composition
# as Salary object HAS A relation wiht EmployeeOne Object in Aggregation
# while
# Salary object IS A PART OF EmployeeOne Object in Composition
# So
# If we delete EmployeeOne Object
# Salary will get deleted in Composition
# But it will remain in Aggregation which can be used elsewhere.

# Source
# https://www.geeksforgeeks.org/python-oops-aggregation-and-composition/?ref=rp

# =============================================================================
# Concept of Aggregation
# Aggregation is a concept in which an object of one class can own or access
#  another independent object of another class. 
# 
# It represents Has-A’s relationship.
# It is a unidirectional association i.e. a one-way relationship. For example,
#  a department can have students but vice versa is not possible and thus
#  unidirectional in nature.
# In Aggregation, both the entries can survive individually which means ending
#  one entity will not affect the other entity.
# 
# =============================================================================

# Code to demonstrate Aggregation

# Salary class with the public method
# annual_salary()
class Salary:
	def __init__(self, pay, bonus):
		self.pay = pay
		self.bonus = bonus

	def annual_salary(self):
		return (self.pay*12)+self.bonus


# EmployeeOne class with public method
# total_sal()
class EmployeeOne:

	# Here the salary parameter reflects
	# upon the object of Salary class we
	# will pass as parameter later
	def __init__(self, name, age, sal):
		self.name = name
		self.age = age

		# initializing the sal parameter
		self.agg_salary = sal # Aggregation

	def total_sal(self):
		return self.agg_salary.annual_salary()

# Here we are creating an object
# of the Salary class
# in which we are passing the
# required parameters
salary = Salary(10000, 1500)

# Now we are passing the same
# salary object we created
# earlier as a parameter to
# EmployeeOne class
emp = EmployeeOne('Geek', 25, salary)

print(emp.total_sal())
