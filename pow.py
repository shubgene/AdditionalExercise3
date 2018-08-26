# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 22:58:22 2018

@author: shurastogi
"""
class MathOperation:
    def __init__(self):
        pass
    
    def pow(self,x,n):
        negative=False
        power=0
        if(n<0 and n!=0):
            negative=True
            n=n*-1
        if (n == 0):
            return 1
        elif (int(n % 2) == 0):
            power= (pow(x, int(n / 2)) * pow(x, int(n/ 2)))
        else:
            power= (x * pow(x, int(n / 2)) * pow(x, int(n / 2)))
        if(negative):
            power=float(1/power)
        return power
        
        
M=MathOperation()
print(M.pow(2,3))
print(M.pow(5, -3))
print(M.pow(-2, 5))
print(M.pow(-5, -3))
print(M.pow(20000,0))