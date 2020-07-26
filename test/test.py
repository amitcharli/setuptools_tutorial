# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:18:26 2020

@author: Amit
"""

from setup_demo.main import demo


def test_square():
    a= demo(3)
    print(a.squared)
    assert a.squared == 9, "The value should be 9"

def test_cube():
    a= demo(10)
    print(a.cubed)
    assert a.cubed == 1000, "The value should be 1000"

def test_factorial():
    a= demo(5)
    print(a.fact)
    assert a.fact == 120, "The value shaould be 120"


if __name__=="__main__":
    test_square()
    test_cube()
    test_factorial()
    print("Congratulations! all tests are passed!")
