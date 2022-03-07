import sys

lis = list(map(int,sys.stdin.readlines()))
lis_max= max(lis)
print(lis_max,1+lis.index(lis_max), sep='\n')

