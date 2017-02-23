# Given: Three positive integers k, m, and n, representing a population containing 
#   k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
#
# Return: The probability that two randomly selected mating organisms will produce 
#   an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
#
# Mateusz Dobrychlop, Krzysztof Formanowicz 2014

import sys

k, l, m = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

s = float(k + l + m)

HOMHOM = (k/s) * ((k-1)/(s-1))

HetHet = ((l/s) * ((l-1)/(s-1))) * 0.75 

HetHOM = ((l/s) * (k/(s-1))) + ((k/s) * (l/(s-1)))

Hethom = (((l/s) * (m/(s-1))) + ((m/s) * (l/(s-1)))) * 0.5

HOMhom = ((k/s) * (m/(s-1))) + ((m/s) * (k/(s-1)))


print HOMHOM + HetHet + HetHOM + Hethom + HOMhom





