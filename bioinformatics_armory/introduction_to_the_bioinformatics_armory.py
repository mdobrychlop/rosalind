# Given: A DNA string s of length at most 1000 bp.
#
# Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
#
# Mateusz Dobrychlop 2014

import sys
from Bio.Seq import Seq

inp_str = sys.argv[1]

seq = Seq(inp_str)

print seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")
