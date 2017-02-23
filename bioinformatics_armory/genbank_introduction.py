# Given: A genus name, followed by two dates in YYYY/M/D format.
#
# Return: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified. subsection of the protein's "Gene Ontology" (GO) section)..
#
# Mateusz Dobrychlop 2014

import sys
from Bio import Entrez

organism = sys.argv[1]
date1 = sys.argv[2]
date2 = sys.argv[3]

Entrez.email = "your_name@your_mail_server.com"
#handle = Entrez.esearch(db="nucleotide", term="\'\""+organism+"\"[Organism]")
handle = Entrez.esearch(db="nucleotide", term='"Zea mays"[Organism] AND rbcL[Gene]')
record = Entrez.read(handle)
record["Count"]
