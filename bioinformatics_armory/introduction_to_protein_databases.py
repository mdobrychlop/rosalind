# Given: The UniProt ID of a protein.
#
# Return: A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section)..
#
# Mateusz Dobrychlop 2014

import sys
from Bio import ExPASy
from Bio import SwissProt

uniprot_id = sys.argv[1]

handle = ExPASy.get_sprot_raw(uniprot_id)

record = SwissProt.read(handle)

for ref in record.cross_references:
    if ref[0] == "GO":
        if ref[2][0:2] == "P:":
            print ref[2][2:]
