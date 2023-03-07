#10773
import sys
stk = []
n = int(sys.stdin.readline())

for x in range(n) :
    a = int(sys.stdin.readline())
    if a != 0 :
        stk.append(a)
    else :
        stk.pop()
print(sum(stk))