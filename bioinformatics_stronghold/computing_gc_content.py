# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
#   Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
#
# Mateusz Dobrychlop 2014

import sys

inp_file = open(sys.argv[1],"r")
inp_string = inp_file.read()

sequences = {}

for record in inp_string.split(">"):
    head = record.split("\n")[0]
    seq = record.split("\n")[1:]
    seq = "".join(seq)
    if seq != "":
        sequences[head] = seq

hi_content = ["no_head",0.0]

for head in sequences:
    g_c = sequences[head].count("G")
    c_c = sequences[head].count("C")
    gc_c = g_c + c_c
    perc_count = (float(gc_c) / len(sequences[head])) * 100

    if perc_count > hi_content[1]:
        hi_content[1] = perc_count
        hi_content[0] = head

print hi_content[0]
if len(str(hi_content[1])) > 9:
    print str(hi_content[1])[:9]
else:
    print hi_content
