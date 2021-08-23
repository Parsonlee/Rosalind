from Bio.Seq import Seq

with open('rosalind_revc.txt', 'r') as file_object:
    seq = file_object.read()

my_seq = Seq(seq)
print(my_seq.reverse_complement())