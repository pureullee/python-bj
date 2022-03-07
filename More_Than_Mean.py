import sys

c = int(input())
for i in range(c) :
    n , *a = map(int,sys.stdin.readline().split())
    outstanding_list = [i for i in a if i > sum(a)/len(a)]
    print("{:0.3f}%".format(len(outstanding_list)/len(a)*100))

