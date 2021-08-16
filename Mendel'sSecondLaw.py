# AaBb基因型的概率在每代中都是0.25，因此失败的概率为0.75
# 二项分布
from scipy.special import comb
def probablity(k, n):
  i = 0
  p = 0
  m = 2 ** k
  for i in range(n, m+1):
    p += comb(m, i) * (0.25 ** i) * (0.75 ** (m-i))
  return p

print(probablity(5,9))