from Bio.Seq import Seq

with open('rosalind_prot.txt', 'r') as file_object:
    seq = file_object.read()

my_seq = Seq(seq)
print(my_seq.translate(to_stop=True))