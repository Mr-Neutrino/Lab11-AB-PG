# https://github.com/Mr-Neutrino/Lab11-AB-PG
# Partner 1: Alessandro Barbieri
# Partner 2: Prabhav Govindu

import math


def add(a, b):
   return a + b


def subtract(a, b):
   return a - b


def multiply(a, b):
   return a * b


def divide(a, b):
   try:
       return b / a
   except ZeroDivisionError as e:
       print(e)


def logarithm(a, b):
   try:
       return math.log(b, a)
   except ValueError as e:
       print(e)


def exponent(a, b):
   return a ** b