import re # for regex functions
import urllib3
from Bio import SeqIO

# need regex for N-glycosylation motif
# N{any but P}[S or T]{any but P}
# parentheses and '?=' allow for overlapping
motif = re.compile('(?=N[^P][ST][^P])')
uniprot_url = "http://www.uniprot.org/uniprot/"
http = urllib3.PoolManager()

with open('rosalind_mprt.txt', 'r') as dataset:
  protein_ids = dataset.readlines()
  ids = [id.strip() for id in protein_ids]

# create a file stroes pure sequences
fas = open('fastas.txt', 'w')
outhandle = open('016_MPRT.txt', 'w')

# loop through protein id's to import from uniprot website
for id in protein_ids:
  url = uniprot_url + id.rstrip() + '.fasta'
  f = http.request('GET', url)
  # print(f.data.decode())
  fas.write(f.data.decode())
fas.close()

seqs = {}
for i, record in enumerate(SeqIO.parse('fastas.txt', 'fasta')):
  # seqs.append(str(record.seq))
  seqs[ids[i]] = str(record.seq)


for id, seq in seqs.items():
  locations = []
  # Use search instead of match to search entire string
  if re.search(motif, seq):
    print(id, file=outhandle)
    for m in re.finditer(motif, seq):
        locations.append(m.start()+1)
    print(" ".join(map(str, locations)), file=outhandle)
outhandle.close()