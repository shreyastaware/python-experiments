#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 00:06:19 2022

@author: shreyastaware
"""

# =============================================================================
# Also an example of Multi Level Inheritance as 
# Animal inherits from canSwim which inherits from Mammal
# Multiple as 
# Animal inherits from canSwim and canFly
# =============================================================================

class Mammal():

	def __init__(self, name):
		print(name, "Is a mammal")


class canFly(Mammal):

	def __init__(self, canFly_name):
		print(canFly_name, "cannot fly")

		# Calling Parent class
		# Constructor
		super().__init__(canFly_name)


class canSwim(Mammal):

	def __init__(self, canSwim_name):

		print(canSwim_name, "cannot swim")

		super().__init__(canSwim_name)


class Animal(canFly, canSwim):

	def __init__(self, name):

		# Calling the constructor
		# of both the parent
		# class in the order of
		# their inheritance
		super().__init__(name)


# Driver Code
Carol = Animal("Dog")

