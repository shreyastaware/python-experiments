#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 00:14:53 2022

@author: shreyastaware
"""

# this is the class which will become
# the super class of "Subclass" class
class Class():
	def __init__(self, x):
		print(x)

# this is the subclass of class "Class"
class SubClass(Class):
	def __init__(self, x):

		# this is how we call super
		# class's constructor
		super().__init__(x)

# driver code
x = [1, 2, 3, 4, 5]
a = SubClass(x)

