import sys


lis=[]

s = sys.stdin.readline().upper()

for i in range(26) :
    lis.append(s.count(chr(ord('A')+i)))
    
if lis.count(max(lis)) >= 2 :
    print('?')
    
else :
    print(chr(ord('A')+lis.index(max(lis))))


