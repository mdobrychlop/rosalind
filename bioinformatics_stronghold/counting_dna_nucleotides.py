# Given: A DNA string s of length at most 1000 nt.
#
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
#
# Mateusz Dobrychlop, 2014

import sys

inp_string = sys.argv[1]

a_count = 0
c_count = 0
g_count = 0
t_count = 0

for char in inp_string:
    if char == "A":
        a_count += 1
    elif char == "C":
        c_count += 1
    elif char == "G":
        g_count += 1
    elif char == "T":
        t_count += 1
        
print a_count, c_count, g_count, t_count
  