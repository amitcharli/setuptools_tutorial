# -*- coding: utf-8 -*-
"""
Created on Fri May  8 01:05:37 2020

@author: Amit
"""

class demo:
    def __init__(self, x):
        self.x =x
        self.fact =1
        self.squared = self.square()
        self.cubed = self.cube()
        self.fact = self.factorial()
    
    def square(self):
        return self.x*self.x
    
    def cube(self):
        return self.x*self.x*self.x
    
    def factorial(self):
        
        for i in range(1,self.x+1):
            self.fact *= i
        
        return self.fact
    