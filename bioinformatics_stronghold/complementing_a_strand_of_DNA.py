# Given: A DNA string s of length at most 1000 bp.
#
# Return: The reverse complement s^c of s.
#
# Mateusz Dobrychlop, 2014

import sys

inp_string = sys.argv[1]

complementary = {"A":"T","T":"A","C":"G","G":"C"}

out_string = ""

for char in inp_string:
    out_string += complementary[char]

out_string = out_string[::-1]

print out_string
