import sys


t = int(input())

for i in range(t) :
    r, s = sys.stdin.readline().split()
    s_list = list(s)
    result = list(map(lambda x : int(r) * x, s_list ))
    print("".join(result))