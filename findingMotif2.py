from __future__ import print_function
import re # for regex functions

# need regex for N-glycosylation motif
# N{any but P}[S or T]{any but P}
# parentheses and '?=' allow for overlapping
motif = re.compile('(?=N[^P][ST][^P])')

# loop through protein id's to import from uniprot website
import urllib3
from Bio import SeqIO

dataset = open("rosalind_mprt.txt", 'r')
protein_ids = dataset.readlines()
dataset.close()

outhandle = open("016_MPRT.txt", 'w')
uniprot_url = "http://www.uniprot.org/uniprot/"
http = urllib3.PoolManager()
url = uniprot_url + 'B5ZC00' + ".fasta"
f = http.request('GET', url)
raw_data = SeqIO.read(f.data, 'fasta')
print(raw_data)
# for protein in protein_ids:
#     url = uniprot_url+protein.rstrip()+".fasta"
#     f = http.request('GET', url)
#     raw_data = SeqIO.read(f.data, 'fasta')

#     locations = []
#     # Use search instead of match to search entire string
#     if re.search(motif, str(raw_data.seq)):
#         print(protein.strip(), file=outhandle)
#         for m in re.finditer(motif, str(raw_data.seq)):
#             locations.append(m.start()+1)
#         print(" ".join(map(str, locations)), file=outhandle)
        
# outhandle.close()