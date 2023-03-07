#1037
import sys


a = int(input())
b = list(map(int,sys.stdin.readline().split()))
print(min(b)*max(b))