# Given: A positive integer n<=25.
#
# Return: The value of Fn.
#
# Mateusz Dobrychlop 2014

import sys

inp_int = int(sys.argv[1])

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(inp_int)



