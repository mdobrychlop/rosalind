# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#
# Return: The Hamming distance dH(s,t).
#
# Mateusz Dobrychlop, 2014

import sys

inp_string = sys.argv[1]

seq1 = inp_string.split("\n")[0]
seq2 = inp_string.split("\n")[1]

i = 0

dist = 0

while i < len(seq1):
    if seq1[i] != seq2[i]:
        dist += 1
    i += 1
    
print dist