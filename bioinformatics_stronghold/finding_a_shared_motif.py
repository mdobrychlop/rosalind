# Given: A collection of k (k<=100) DNA strings of length at most 1 kbp each in FASTA format.
#
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
#
# Mateusz Dobrychlop, 2014

import sys

def find_all_substrings(string):
    all_substrings = []
    i = 0
    while i < len(string):
        sub_long = string[i:]
        print sub_long
        if sub_long not in all_substrings:
            all_substrings.append(sub_long)
        j = -1
        while j*-1 < len(sub_long):
            sub_short = string[i:j]
            print sub_short
            if sub_short not in all_substrings:
                all_substrings.append(sub_short)
            j -= 1
        i += 1
    
    print "SUBSTRINGS DONE."
    
    return all_substrings

###############################################################################

def find_all_substrings_2(string):
    all_substrings = [string]
    i = 1
    wins = 1
    while i < len(string):
        print "XXX", i
        s_i = i-1
        for j in range(s_i*-1,s_i):
            print s_i-j, j
        s_i
        i+=1



inp_file = open(sys.argv[1], "r")

inp_string = inp_file.read()

sequences = []

for record in inp_string.split(">"):
    seq = record.split("\n")[1:]
    seq = "".join(seq)
    if seq != "":
        sequences.append(seq)

shortest_seq = min(sequences, key=len)

print shortest_seq

sequences.remove(shortest_seq)

motives = find_all_substrings(shortest_seq) ################

common_motives = []

for m in motives:
    present = True
    for s in sequences:
        if m not in s:
            present = False
            break
    if present == True:
        print "COMMON!", m
        common_motives.append(m)

find_all_substrings_2(shortest_seq)


print motives
print common_motives
print "LONGEST:", max(common_motives, key=len)
