# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#
# Return: The protein string encoded by s.
#
# Mateusz Dobrychlop 2014

import sys

inp_file = open(sys.argv[1],"r")
inp_string = inp_file.read()

#inp_string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

gen_code = {"UUU":"F","CUU":"L","AUU":"I","GUU":"V",\
"UUC":"F","CUC":"L","AUC":"I","GUC":"V",\
"UUA":"L","CUA":"L","AUA":"I","GUA":"V",\
"UUG":"L","CUG":"L","AUG":"M","GUG":"V",\
"UCU":"S","CCU":"P","ACU":"T","GCU":"A",\
"UCC":"S","CCC":"P","ACC":"T","GCC":"A",\
"UCA":"S","CCA":"P","ACA":"T","GCA":"A",\
"UCG":"S","CCG":"P","ACG":"T","GCG":"A",\
"UAU":"Y","CAU":"H","AAU":"N","GAU":"D",\
"UAC":"Y","CAC":"H","AAC":"N","GAC":"D",\
"UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E",\
"UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E",\
"UGU":"C","CGU":"R","AGU":"S","GGU":"G",\
"UGC":"C","CGC":"R","AGC":"S","GGC":"G",\
"UGA":"Stop","CGA":"R","AGA":"R","GGA":"G",\
"UGG":"W","CGG":"R","AGG":"R","GGG":"G"}

i = 0

prot_seq = ""

while i < len(inp_string):
    codon = inp_string[i:i+3]
    if gen_code[codon] == "Stop":
        break
    prot_seq += gen_code[codon]
    i += 3

print prot_seq
