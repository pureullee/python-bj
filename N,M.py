from itertools import permutations

n, m = map(int,input().split())

per = list(permutations([x+1 for x in range(n)],m))

for i in per :
    
    print(*i)

    