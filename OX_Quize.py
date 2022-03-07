import sys

score = 0

n = int(input())

for i in range(n) :
    s = sys.stdin.readline()
    
    while True :
        a= s.find('X')
        if a == -1 :
            score += len(s)*(len(s)-1)/2
            print(int(score))
            break
        score += a * (a+1) / 2
        s = s[a+1:]
    score = 0