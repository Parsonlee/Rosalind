# 序列第n个位置的碱基和倒数第n个位置的碱基，必然是A-T或者是G-C，这样他反过来互补才能是一样的
# 只要大序列中找到切出小序列满足小序列中所有的正数倒数第n个碱基都是A-T或者G-C，就可以输出。
from Bio import SeqIO
for seq_record in SeqIO.parse('rosalind_revp.fasta','fasta'):
  seq = seq_record.seq

def palindrome(s, k):
	#k must be even numbers
	palindrome_pairs = [('A','T'),('T','A'),('G','C'),('C','G')]
	for i in range(len(s)-k+1):
		test = s[i:i+k]
		if all((test[j],test[k-j-1]) in palindrome_pairs for j in range(k)):
			# print(test, i+1, k)
			print(i+1, k)

for i in range(4,14,2):
	palindrome(seq, i)