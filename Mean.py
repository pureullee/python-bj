import sys

n = int(input())
lis = list(map(int, sys.stdin.readline().split()))
print(sum(lis)/max(lis)*100/n)

