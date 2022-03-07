import sys
n = int(input())
lis = list(map(int,sys.stdin.readline().split()))
print(min(lis), max(lis))
