#1406
import sys

data_left = list(sys.stdin.readline().rstrip()) #처음에 문자열을 전부 받으면 커서의 위치는 data_left 마지막 요소 다음에 위치함.
data_right = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n) :
    cmd = sys.stdin.readline().rstrip()
    
    if cmd[0] == 'L' :
        if data_left :
            data_right.append(data_left.pop())
    elif cmd[0] == 'D' :
        if data_right :
            data_left.append(data_right.pop())
    elif cmd[0] == 'B' :
        if data_left :
            data_left.pop()
    else : # cmd[0] == 'P'
        data_left.append(cmd[2]) 
        

data = data_left if data_right==[] else data_left + list(reversed(data_right)) #data_right가 빈리스트면 data_left만 출력하기위함. 아니라면 뒤집은 data_right를 합쳐줌
print("".join(data))
