# Given: A DNA string s of length at most 1 kbp in FASTA format.
#
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
#
# Mateusz Dobrychlop 2014

import sys

inp_file = open(sys.argv[1],"r")
inp_string = inp_file.read()

#inp_string = """>Rosalind_99
#AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"""

sequences = []
for record in inp_string.split(">"):
    seq = record.split("\n")[1:]
    seq = "".join(seq)
    if seq != "":
        sequences.append(seq)


sequence_5 = sequences[0]
seq3 = sequence_5[::-1]

sequence_3 = ""

for nt in seq3:
    if nt == "A":
        sequence_3 += "T"
    elif nt == "T":
        sequence_3 += "A"
    elif nt == "G":
        sequence_3 += "C"
    elif nt == "C":
        sequence_3 += "G"

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

def trans_one_frame(string, startpos):
    i = startpos

    prot_seq = ""

    while i < len(string):
        codon = string[i:i+3]
        if len(codon) == 3:
            if gen_code_DNA[codon] == "Stop":
                return prot_seq
            prot_seq += gen_code_DNA[codon]
        i += 3
        
def find_all_peptides(sequence):
    atg_positions = []
    peptides = []
    
    i = 0
    
    while i < len(sequence_5):
        if sequence[i] == "A":
            if sequence[i:i+3] == "ATG":
                atg_positions.append(i)
        i += 1
    
    for pos in atg_positions:
        prot = trans_one_frame(sequence,pos)
        if prot != None:
            peptides.append(prot)
            
    return peptides


pepts_3 = find_all_peptides(sequence_3)
pepts_5 = find_all_peptides(sequence_5)

for p in pepts_3:
    if p not in pepts_5:
        pepts_5.append(p)

outfile = open(sys.argv[2],"w")
for p in pepts_5:
    print >> outfile, p



