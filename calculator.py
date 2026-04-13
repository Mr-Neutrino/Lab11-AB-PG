# https://github.com/Mr-Neutrino/Lab11-AB-PG
# Partner 1: Alessandro Barbieri
# Partner 2: Prabhav Govindu

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a
    except:
        raise ZeroDivisionError()

def log(a, b):
    try:
        return math.log(b, a)
    except:
        raise ValueError()

def exp(a, b):
    return a ** b


def add(a, b):
   return a + b


def subtract(a, b):
   return a - b


def multiply(a, b):
   return a * b





def logarithm(a, b):
   try:
       return math.log(b, a)
   except ValueError as e:
       print(e)


def exponent(a, b):
   return a ** b
