#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 01:48:22 2022

@author: shreyastaware
"""

class Person(object):
    
    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num
        
    def display(self):
        print(self.name)
        print(self.id_num)
        
    def details(self):
        print("My name is {}".format(self.name))
        print("My ID Number is {}".format(self.id_num))
        
class Employee(Person):
    
    def __init__(self, name, id_num, salary, post):
        self.salary = salary
        self.post = post
        
        Person.__init__(self, name, id_num)
        """
        Above line is an alternative to - direct assignment
        
        Person.__init__(variable_name, name, id_num)
        
        variable_name should already be a Object
        
        variable_name = Person(name, id_num)
        """
    
    def details(self):
        print("My name is {}".format(self.name))
        print("IDNumber: {}".format(self.id_num))
        print("Post: {}".format(self.post))
            