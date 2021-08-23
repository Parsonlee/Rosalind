import numpy as np
from Bio import SeqIO
from collections import Counter

fh = open('output.txt', 'wt')

seqs = []
for seq_record in SeqIO.parse('Rosalind_cons.fasta', 'fasta'):
    seqs.append(list(seq_record.seq))
seq_matrix = np.array(seqs)

consensus_s = ''
A, C, G, T = [], [], [], []
for i in range(seq_matrix.shape[1]):
    conlumn = [x[i] for x in seq_matrix]
    A.append(conlumn.count('A'))
    C.append(conlumn.count('C'))
    G.append(conlumn.count('G'))
    T.append(conlumn.count('T'))
    consensus_s += Counter(seq_matrix[:, i]).most_common()[0][0]

fh.write(consensus_s + '\n')
fh.write('\n'.join([
    'A:\t' + '\t'.join(map(str, A)), 'C:\t' + '\t'.join(map(str, C)),
    'G:\t' + '\t'.join(map(str, G)), 'T:\t' + '\t'.join(map(str, T))
]))
fh.close()

# print(consensus_s)
# for i,ch in enumerate('AGCT'):
#   s = ' '.join([str(x) for x in r[i]])
#   print(f'{ch}: {s}')