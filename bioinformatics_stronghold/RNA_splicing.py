# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
#
# Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
#
# Mateusz Dobrychlop 2014

import sys

inp_file = open(sys.argv[1],"r")
inp_string = inp_file.read()

#inp_string = """>Rosalind_10
#ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
#>Rosalind_12
#ATCGGTCGAA
#>Rosalind_15
#ATCGGTCGAGCGTGT"""

gen_code_DNA = {"TTT":"F","CTT":"L","ATT":"I","GTT":"V",\
"TTC":"F","CTC":"L","ATC":"I","GTC":"V",\
"TTA":"L","CTA":"L","ATA":"I","GTA":"V",\
"TTG":"L","CTG":"L","ATG":"M","GTG":"V",\
"TCT":"S","CCT":"P","ACT":"T","GCT":"A",\
"TCC":"S","CCC":"P","ACC":"T","GCC":"A",\
"TCA":"S","CCA":"P","ACA":"T","GCA":"A",\
"TCG":"S","CCG":"P","ACG":"T","GCG":"A",\
"TAT":"Y","CAT":"H","AAT":"N","GAT":"D",\
"TAC":"Y","CAC":"H","AAC":"N","GAC":"D",\
"TAA":"Stop","CAA":"Q","AAA":"K","GAA":"E",\
"TAG":"Stop","CAG":"Q","AAG":"K","GAG":"E",\
"TGT":"C","CGT":"R","AGT":"S","GGT":"G",\
"TGC":"C","CGC":"R","AGC":"S","GGC":"G",\
"TGA":"Stop","CGA":"R","AGA":"R","GGA":"G",\
"TGG":"W","CGG":"R","AGG":"R","GGG":"G"}

sequences = []

for record in inp_string.split(">"):
    seq = record.split("\n")[1:]
    seq = "".join(seq)
    if seq != "":
        sequences.append(seq)

main_seq = sequences[0]

del sequences[0]

for s in sequences:
    main_seq = main_seq.replace(s,"")

i = 0

prot_seq = ""

while i < len(inp_string):
    codon = main_seq[i:i+3]
    if gen_code_DNA[codon] == "Stop":
        break
    prot_seq += gen_code_DNA[codon]
    i += 3

print prot_seq
