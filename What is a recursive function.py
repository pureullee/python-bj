#17478

def func(a) :
    
    count = x-a
    print('____' * count,'"재귀함수가 뭔가요?"', sep='')
    if a != 0 :
        print('____' * count,'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n','____' * count,'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n','____' * count,'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."',sep='')
    else :
        print('____'* count,'"재귀함수는 자기 자신을 호출하는 함수라네"',sep='')
        print('____'* count,"라고 답변하였지.",sep='')
        return True
        
    
        
    return func(a-1),print('____'* count,'라고 답변하였지.',sep = '')
        
global x 
x= int(input())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
func(x)
    
    
    
        