#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 21:31:36 2022

@author: shreyastaware
"""

class Dog:

	# class attribute
	attr1 = "mammal"

	# constructor
	def __init__(self, name):
        # Instance attribute
		self.name = name

	def speak(self):
		print("My name is {}".format(self.name))


# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is Mr. {}".format(Rodger.name))
print("My name is Mr. {}".format(Tommy.name))

# Accessing class methods
Rodger.speak()
Tommy.speak()
