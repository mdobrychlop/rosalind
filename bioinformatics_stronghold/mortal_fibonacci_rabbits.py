# Given: Positive integers n<=100 and m<=20.
#
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
#
# Mateusz Dobrychlop 2014

import sys

inp_int1 = int(sys.argv[1])
inp_int2 = int(sys.argv[2])

def mortal_rabbits(n, m):
    
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    else:
        return (mortal_rabbits(n-1,m) + mortal_rabbits(n-2,m)) - mortal_rabbits(n-m,m)

print mortal_rabbits(inp_int1, inp_int2)


#1  2   3   4    5
#1  1   4   7   19
