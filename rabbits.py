month, k = map(int, input().strip().split())
f = [0,1,1]
for x in range(3, month+1):
  f.append(f[-1]+f[-2]*k)
print(f[-1])

# recursion
# def rabbits(n, k):
#   if n <= 2:
#     return 1
#   return rabbits(n-1,k) + rabbits(n-2,k)*k