#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 08:24:24 2022

@author: shreyastaware
"""

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # an instance method
    def can_marry_or_not(self, gender):
        if ( (gender.upper().startswith('M') and self.age >= 21) or 
            (gender.upper().startswith('F') and self.age >= 18) ):
            print("The person can marry")
        else:
            print("The person cannot marry. Person's too young.")
    
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 19)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

print(person1.can_marry_or_not('M'))
print(person2.can_marry_or_not('F'))
