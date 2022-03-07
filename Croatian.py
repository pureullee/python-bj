import sys



line = sys.stdin.readline().strip()

cr = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in cr :
    line = line.replace(i,'0')
    
print(len(line))





    