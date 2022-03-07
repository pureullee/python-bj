s = str(input())

for i in range(26) :
    a = s.find(chr(ord('a')+i))
    print(a, end =' ')
