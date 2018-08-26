# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 18:24:01 2018

@author: shurastogi
"""

class Person:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        
    def __str__(self):
        print("The name is",self.first +" " + self.last)
    
class Employee(Person):
    def __init__(self,first,last):
        super().__init__(first,last)
        super().__str__()
        
e1=Employee("shubham","rastogi")