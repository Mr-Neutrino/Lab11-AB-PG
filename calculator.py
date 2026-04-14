# https://github.com/Mr-Neutrino/Lab11-AB-PG
# Partner 1: Alessandro Barbieri
# Partner 2: Prabhav Govindu

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except:
        raise ValueError()

def hypotenuse(a, b):
    math.hypot(a, b)

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a
    except:
        raise ZeroDivisionError()

def exp(a, b):
    return a ** b

def subtract(a, b):
   return a - b

def logarithm(a, b):
   try:
       return math.log(b, a)
   except:
       raise ValueError()
