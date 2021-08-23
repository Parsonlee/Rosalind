# * 问题：三个正整数k, m和n，代表一个包含k+m+n个有机体的种群:k个个体是一个因子的纯合子显性，m是杂合子，n是纯合子隐性。
# * 所求：两个随机选择的交配生物体产生一个具有显性等位基因的个体的概率。假设任意两个有机体都可以交配。
# * Sample dataset：2 2 2(homozygous  dominant(AA);heterozygous(Aa);homozygous recessive(aa))
# * Result:1-(2C2+1/4*2C2+1/2*2*2)/6C2=0.78333

# * The probability that two randomly selected mating organisms will produce a homozygous recessive(aa) individual : P2
# * Vector A = Possiblity_of selection[(aa,aa),(Aa,Aa),(Aa,aa)] = (2C2/6C2,2C2/6C2,2*2/6C2)
# * Vector B = Possbility_of_producing_aa[aaxaa,AaxAa,Aaxaa] = (1,1/4,1/2)
# * P2 = Vector A * Transpose of Vector B
# * P2= (2C2+1/4*2C2+1/2*2*2)/6C2 = 0.21667
# * So the probability that two randomly selected mating organisms will produce an individual possessing a dominant allele: P1
# * P1 = 1-P2 =0.78333


def f(x, y, z):
    s = x + y + z  # the sum of population
    c = s * (s - 1) / 2.0  # comb(2,s)
    p = 1 - (z * (z - 1) / 2 + 0.25 * y * (y - 1) / 2 + y * z * 0.5) / c
    return p


print(f(21, 19, 24))
