# Given: Six positive integers, each of which does not exceed 20,000.
#       The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor.
#       In order, the six given integers represent the number of couples having the following genotypes:
#           AA-AA
#           AA-Aa
#           AA-aa
#           Aa-Aa
#           Aa-aa
#           aa-aa
#
# Return: The expected number of offspring displaying the dominant phenotype
#       in the next generation, under the assumption that every couple has exactly two offspring.
#
# Mateusz Dobrychlop 2014

import sys

a = int(sys.argv[1]); b = int(sys.argv[2]); c = int(sys.argv[3])
d = int(sys.argv[4]); e = int(sys.argv[5]); f = int(sys.argv[6])

HOMHOM = 1.0
HetHOM = 1.0
HOMhom = 1.0
HetHet = 0.75
Hethom = 0.5
homhom = 0.0


print (HOMHOM*a + HetHOM*b + HOMhom*c + HetHet*d + Hethom*e + homhom*f) * 2





