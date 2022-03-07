import sys

ls = sys.stdin.readlines()
t = int(ls[0])
del ls[0]

for i in range(t):
    a,b= map(int,ls[i].split())
    ls[i] = "Case #"+str(i+1)+": "+ str(a) + ' + ' + str(b) +' = '+str(a+b)+'\n'
    
print(''.join(ls))




    




    


