#!/usr/bin/env python
""" This is my annotation for nevermore forget Edit """

def fibonacci(number=None):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if counter > number: return
        yield a
        a, b = b, a + b
        counter += 1

if __name__ == '__main__':
    fib = fibonacci(5)
    for x in fib:
        print [x,]