seq1 = "GTCATGCCTAGTGAGCGAAGATATGTACAGAGAACAAAGTTGAAGAAGGTCTTTGGAAACACTTTTGCACTATCTCATCGCGTACGATGAACACTAACTCGGGTCTAGGTAGTCGTACAGCAATTTCATCACGCACCCGTAGCTGGGTGTAAGAACCTAGCCTTATAGCCTTCTCCGCTAAATATAACTCGGTATACGGGGGGGGCTCGTGTAGTGCTTCAGTTATAGAAATTGAACCTTGGCTTATATCAGAAGCCTCTTGCCTCGATTTCGTGTCGAGAGAGGACAATAGATGGAGCCCATAGAAACTTAAACGTGGCTTCGGTCCCTCATGGAAAAACTAGCAATGTTACAGGACACGCACTGACGAGACTATCCCTGTTAACGAAATACCACTGGGAGTGATTTTTTCCAAAAGGGGGGACTGACCTAGGAACATTGCTACGTTCTATATGGGCCCGTCACTAGTCTTATCCGATCGTGACCTGGCCGAGCCTCTACTTATATATTCCATTATAATGGCGAGTTCGGAGAAAGAGACGAATTTATGCTATCGATTACTCCCATGGGAGCGGAGTGGCTGCGGTTATTCATATCTGCCACCTCATCCTACGGCATTTGCAGGCTCCACTGGGAAGGGATTTCCAGAGCGACATCGACCATCGTGAATTATGCTGGTAGCGGCGTGGACGTACGCGACATACATTGTGTCGGTCCGGAGAAATTCGCCATCGCGCCGCGTCGGTATGTATATTGGGCAGGAAAGATACCGAGAAGTTCACTCTACGCGAACTCGGGTGCGAACATGAATTACATAGTAGATGCCCACAGGTTGAATAGCGCCTTACAGAGTAGTGGTCTCTACTGTGCCATACGGAAACACGTGGGAGTTTCCTGCAGAGGAGAGTCGCACGGAAAGCGACCCCTAGCAGCATAAGTACATTACCGTCTTAATAGTTGGTACTTGCGACGTCAGTTTC"
seq2 = "TGGCAGCCGTATCATCGAAGTTACATCCAGATTACTAGATGTCTTCTTGTTCATCGTAATACGGGTGAATCAGCGCGTGCTGTAACTCGCGGGCGAAATCCAAAGGCCGAAGGTGCACATGAGATTCCGCACGTTCCCAGCGCTGGATGAACACCCTATGACTAATAGTATTAGCCCTCCACAATCACTTTTCATTCGCTAGGTGTTCTTTTGGCGCTCCAGATATATGTCCAGAGAACTGGCATCTAGACTCGATCCCGCGGAGGGATCGCGGGGCTAGCTATGCTAACAATCGAAGCAAGTAACTGCTACATCGTGTTGTCAGTGAGTTACAGAACTTATCGCAAAGCGACGTAACATGAGCAGTAATAACTAGCCCCAAAGGCCGTCTTAGAATAGCCGTGATTGTCGACGAACATGAGAATTGACCCTGGTGCTACGCTCCGTTCCACGTCTGCCCGTAACTAGATCTCATTGAGCGGTACGCGCCCGGACATCTGCCCATGTATCCTAAAAACATGGGCACGGCGGAGAGACAGACCTCTGTTGGCGGCCTAATCCCACTTACAGATTACATTGGCATCCGCTAACCGAACTATATGCCCCATGCAACACTGCAACCAGTCGGCTCATGGATGGGAAGTCCTGAGCGCCCTCCTGCGGGGTGCGTCGTCGTGGGTCCTAAGTGGGCGGACCGCCCATACACACTAACGGACAGGAATAATAAGCAATAATCACCCGTCGGTATGAATATGGGCCAGGTAGGTCCCTCCACCCTTCACTATAGTCGACCTCAGGTTCGCACACCAGACGCATGTAGCCTGCGGACGGGCTGACTAACGCCTTCTCGTGCAATGGCCCCCGCTGATGCATGATCTCTAACCTGAGAGTGCTGCGTTGAAGAGACTGTACTTGAACGTCGACGGTAATACCGGTTATACAGTTATGACGTCATTGGCCGTACTAAAATTGACGAATTT"
mutations = 0
for i in range(len(seq1)):
  if seq1[i] != seq2[i]:
    mutations+=1

print(mutations)