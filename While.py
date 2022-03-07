import sys

while True :
    data = sys.stdin.readline()
    
    if not data : break
    
    a, b = map(int,data.split())
    print(a+b)
    