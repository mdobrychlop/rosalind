# Given: Two DNA strings s and t (each of length at most 1 kbp).
#
# Return: All locations of t as a substring of s.
#
# Mateusz Dobrychlop, 2014

import sys

inp_string = sys.argv[1]

seq1 = inp_string.split("\n")[0]
seq2 = inp_string.split("\n")[1]

sub_start = seq2[0]
sub_len = len(seq2)

positions = []

i = 0

while i < len(seq1):
    if seq1[i] == sub_start:
        if seq1[i:i+sub_len] == seq2:
            positions.append(str(i+1))
    i += 1

out = " ".join(positions)

print out