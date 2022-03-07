lis = [int(input()) for i in range(3)]
answer = lis[0] * lis[1] * lis[2]

answer_string = list(str(answer))

for i in range(10) :
    print(answer_string.count(str(i)))