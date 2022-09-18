#!/usr/bin/python3

def add_integer(a, b=98):
    try:
        if type(a,b) == int or float:
            continue
        elif type(a,b) == float:
            a = int(a)
            b = int(b)

            sum = a+b
            return sum
    except TypeError:
        print('a must be an integer\nb must be an integer')




