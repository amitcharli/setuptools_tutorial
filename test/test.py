# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:18:26 2020

@author: Amit
"""

from setup_demo.main import demo
import pytest
import logging


def test_square(capfd):
    a= demo(3)
    logging.info("Squared")
    assert a.squared == 9, "The value should be 9"

def test_cube(capfd):
    a= demo(10)
    logging.info("Cubed")
    assert a.cubed == 1000, "The value should be 1000"

def test_factorial(capfd):
    a= demo(5)
    logging.info("calculated factorial")
    assert a.fact == 120, "The value shaould be 120"


if __name__=="__main__":
    test_square(None)
    test_cube(None)
    test_factorial(None)
    logging.info("all tests performed")
