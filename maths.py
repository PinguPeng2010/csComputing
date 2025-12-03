"""Small math utilities used for examples and exercises.

This module contains multiple small functions. Each function returns
its computed result instead of printing so callers can handle output
consistently (printing, logging, or further processing).
"""

import math


def makealbertpresident(A, B, C, D):
        """Compute and return four derived values from inputs.

        Parameters
        - A, B, C, D: numeric inputs

        Returns
        - tuple of four numeric values (a, b, c, d) computed as:
            a = A + D
            b = A*C - 3*B
            c = (A*B)**2
            d = (C*D) / (A*B)
        """
        # Simple intermediate computations returned as a tuple
        a = (A + D)
        b = ((A * C) - (3 * B))
        c = ((A * B) * (A * B))
        d = ((C * D) / (A * B))
        return a, b, c, d

def cuboidvolume(a, b, c):
    """Return the volume of a cuboid with sides a, b, and c.

    Parameters
    - a, b, c: lengths of the cuboid edges (numeric)

    Returns
    - volume (numeric)
    """
    cuboidv = (a * b * c)
    return cuboidv

def add_numbers(a,b):
    print(a+b)
add_numbers(-3,4)
 
def times_numbers(a,b):
    print(a*b)
 
times_numbers(-3,4)
 
def subtract_numbers(a,b):
    print(a-b)
subtract_numbers(-8,-6)
 
def divide_numbers(a,b):
    print(a/b)

def ratiogb(g,b):
    """Compute and return four times the sum of g and b.

    This appears to be a simple ratio helper used elsewhere.
    """
    c = ((g + b) * 4)
    return c

def isPrime(n):
    """Return the list of prime factors of integer n.

    The original implementation printed prime factors. This version
    returns them as a list so callers can decide how to format output.

    Parameters
    - n: integer or string representing an integer

    Returns
    - list of prime factors (integers). Returns empty list for n < 2.
    """
    n = int(n)
    factors = []
    if n < 2:
        return factors
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def two_digits_and_squares():
    squares = []
    for x in range(100):
        squares.append(x**2)
    count = 0
    for x in range(10,100):
        for i in range(10,100):
            num = x*i
            if num in squares:
                count += 1
    return count

def isSquare(x):
    """Return True if the two-digit integer x has identical digits.

    Parameters
    - x: integer or string representing an integer

    Returns
    - True if x is a two-digit number and both digits are equal,
      otherwise False.

    Raises
    - ValueError if x is not a two-digit integer (10..99).
    """
    x = int(x)
    if x < 10 or x > 99:
        raise ValueError("Input must be a two-digit integer")
    arr = list(str(x))
    return arr[0] == arr[1]
 
def cylinder(d, h):
        """Return the cross-sectional area, volume and capacity of a cylinder.

        Parameters
        - d: diameter of the cylinder (numeric)
        - h: height of the cylinder (numeric)

        Returns
        - tuple (area_cm2, volume_cm3, capacity_ml)

        Notes
        - Uses math.pi for the area calculation. 1 cm^3 == 1 ml, so capacity
            is returned in millilitres equal to the volume in cubic centimetres.
        """
        d = float(d)
        h = float(h)
        area = (math.pi * (d / 2) ** 2)
        volume = area * h
        capacity_ml = volume
        return area, volume, capacity_ml



def main():
    print('cool')
    calc = input('>>> ')
    quit = False
    try:
        # Minimal interactive entry point retained for compatibility.
        # This function is intentionally minimal and not used by library callers.
        print('cool')
        calc = input('>>> ')
        quit = False
        try:
            while not quit:
                args = calc.split(' ')

                if args[0] == 'albert':
                    # capture and display returned results
                    result = makealbertpresident(2, -3, 0.5, -12)
                    print(result)

                elif args[0] == 'digitSquare':
                    print(two_digits_and_squares())

                elif args[0] == 'isSquare':
                    print(isSquare(args[1]))

                elif args[0] == 'cylinder':
                    print(cylinder(args[1], args[2]))

                elif args[0] == 'prime':
                    print(isPrime(args[1]))
            
                # break after single iteration (original loop did not update input)
                break








