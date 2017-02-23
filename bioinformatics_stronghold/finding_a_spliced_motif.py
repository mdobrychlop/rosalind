# Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
#
# Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
#
# Mateusz Dobrychlop 2014

import sys

inp_file = open(sys.argv[1],"r")
inp_string = inp_file.read()

#inp_string = """>Rosalind_14
#ACGTACGTGACG
#>Rosalind_18
#GTA"""

sequences = []

for record in inp_string.split(">"):
    seq = record.split("\n")[1:]
    seq = "".join(seq)
    if seq != "":
        sequences.append(seq)

main_seq = sequences[0]

motif = sequences[1]

positions = []

add = 0

for nt in motif:
    pos = main_seq.find(nt)
    positions.append(str(pos + add + 1))
    main_seq = main_seq[pos+1:]
    add += pos+1

print " ".join(positions)
