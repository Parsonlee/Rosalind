from Bio.SeqUtils import GC
from Bio import SeqIO

dict = {}
for seq_record in SeqIO.parse("rosalind_gc.fasta", "fasta"):
    dict[seq_record.id] = GC(seq_record.seq)

print(max(dict, key=dict.get))  # 返回最大值对应的键
print(dict[max(dict, key=dict.get)])