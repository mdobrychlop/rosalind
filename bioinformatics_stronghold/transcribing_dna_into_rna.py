# Given: A DNA string t having length at most 1000 nt.
#
# Return: The transcribed RNA string of t.
#
# Mateusz Dobrychlop, 2014

import sys

inp_string = sys.argv[1]

out_string = ""

for char in inp_string:
    if char == "T":
        out_string += "U"
    else:
        out_string += char
        
print out_string