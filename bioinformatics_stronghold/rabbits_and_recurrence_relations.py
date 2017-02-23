# Given: Positive integers n<=40 and k<=5.
#
# Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation,
#       every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
#
# Mateusz Dobrychlop 2014

import sys

inp_int1 = int(sys.argv[1])
inp_int2 = int(sys.argv[2])

def rabbits(n, k):
    if n <= 2:
        return 1
    else:
        return rabbits(n-1,k) + (rabbits(n-2,k) * k)

print rabbits(inp_int1, inp_int2)


#1  2   3   4    5
#1  1   4   7   19
