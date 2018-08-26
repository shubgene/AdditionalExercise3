# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 21:48:53 2018

@author: shurastogi
"""

class Cone:
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
        
    def area_of_cone(self):
        pi=3.14159265
        area=float(pi*self.radius*(self.radius+((self.height**2+self.radius**2)**(1/2.0))))
        print("Area of cone with radius: {} and height: {} is : {}".format(self.radius,self.height,area))



radius_input=float(input("Please enter the radius of the cone:"))
height_input=float(input("Please enter the height of the cone:"))
cone_object=Cone(radius_input,height_input)
cone_object.area_of_cone()
