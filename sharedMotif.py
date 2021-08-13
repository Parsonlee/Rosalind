from Bio import SeqIO

# seqs stores the sequences
seqs = []
for sr in SeqIO.parse('rosalind_lcsm.txt','fasta'):
  seqs.append(str(sr.seq))

def checkSubstring(find_str, str_list):
  """Checks if a given substring appears in all members of a given collection of strings and returns True/False."""
  for string in str_list:
    if (len(string) < len(find_str)) or find_str not in string:
      return False
  return True

def longestSubString(str_list):
  longest = ''
  """Extracts all substrings from the first string in a list, and sends longest substring candidates to be checked."""
  for start_idx in range(len(str_list[0])):
    for end_idx in range(len(str_list[0]), start_idx, -1):
      if end_idx - start_idx <= len(longest):
        break
      elif checkSubstring(str_list[0][start_idx:end_idx], str_list[1:]):
        longest = str_list[0][start_idx:end_idx]
  return longest

lcsm = longestSubString(seqs)
print(lcsm)