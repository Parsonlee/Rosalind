import re
from collections import OrderedDict


def overlap_graph(dna, n):
    edges = []
    for ke1, val1 in dna:
        for ke2, val2 in dna:
            if ke1 != ke2 and val1[-n:] == val2[:n]:
                edges.append(ke1 + ' ' + ke2)
    return edges


seq = OrderedDict()
with open('rosalind_grph.txt') as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('>'):
            seqName = re.sub('>', '', line)
            seq[seqName] = ''
            continue
        seq[seqName] += line.upper()

dna = seq.items()
fh = open('rosalind_grph_output.txt', 'wt')
for x in overlap_graph(dna, 3):
    fh.write(x + '\n')
    # print(x, end='\n')
fh.close()