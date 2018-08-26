# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 18:12:39 2018

@author: shurastogi
"""

class Base:
    def __init__(self):
        pass
    
class Derived(Base):
    def __init__(self):
        pass
    

derived=Derived()
baseClass=Base()
print(issubclass(Derived,Base))
print(issubclass(Base,Derived))
print(isinstance(baseClass,Derived))
print(isinstance(derived,Base))
