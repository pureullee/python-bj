import sys


a, b = sys.stdin.readline().split()

if a[::-1] > b[::-1] :
    print("".join(a[::-1]))
else :
    print("".join(b[::-1]))

