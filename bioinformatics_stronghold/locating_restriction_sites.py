# Given: A DNA string of length at most 1 kbp in FASTA format.
#
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12.
#
# Mateusz Dobrychlop 2014

import sys

inp_file = open(sys.argv[1],"r")
inp_string = inp_file.read()

#inp_string = """>Rosalind_24
#TCAATGCATGCGGGTCTATATGCAT"""

sequences = []
for record in inp_string.split(">"):
    seq = record.split("\n")[1:]
    seq = "".join(seq)

def get_reverse_complement(inseq):
    outseq = ""
    for nt in inseq:
        if nt == "A":
            outseq += "T"
        elif nt == "T":
            outseq += "A"
        elif nt == "G":
            outseq += "C"
        elif nt == "C":
            outseq += "G"
    
    outseq = outseq[::-1]
    return outseq

def search_for_palindromes(inseq, length):
    i=0
    while i < len(inseq):
        candidate = inseq[i:i+length]
        if len(candidate) == length:
            if candidate == get_reverse_complement(candidate):
                print i+1, len(candidate)
                #print candidate
                #print get_reverse_complement(candidate)
        i += 1

for n in range(4,13):
    search_for_palindromes(seq,n)


