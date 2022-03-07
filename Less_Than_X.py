import sys

n, x = map(int,sys.stdin.readline().split())
lis = sys.stdin.readline().split()
lis_i = map(int, lis)
lis_answer = [i for i in lis_i if i < x ]
lis_s = map(str, lis_answer)
print(' '.join(lis_s))









