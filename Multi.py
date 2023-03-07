import sys


time = 0

class Cpu :
    exit_count = 0 ## -1을 만나면 1 증가시키는 클래스 변수
    wake_count = 0
    Cpu_count = 0
    status = 0 ## 0은 cpu 할당 가능상태 , 1은 io 상태 인스턴스 변수, 2는 종료
    index = 0 ## task 리스트에 접근할 때 쓰이는 인덱스
    io_time = 0
    
    def __init__(self, task) :
        self.task = task
        self.wait_time = 0 ## cpu 작업 후 io가 끝나는 시점
        self.num = Cpu.Cpu_count
        Cpu.Cpu_count +=1
        
        
    def tasking(self) :
        global time
        
        if self.task[self.index] != -1 :
            time += self.task[self.index]
            print(f'{self.num}번째 Cpu가{self.task[self.index]}의 작업을 하였습니다. ')
            print(f'현재 시각은 {time}입니다.')
            
            if self.task[self.index + 1] == -1 :
                print(f'{self.num}번째 Cpu가 종료하였습니다.')
                Cpu.exit_count += 1
                self.status = 2
                Cpu.io_time = 0
            else :
                self.status = 1 
                self.wait_time = time + self.task[self.index + 1]
                print(f'{self.num}번째 Cpu가 {self.wait_time}까지 IO 상태에 있습니다.')
                
                if self.task[self.index + 2] == -1 :
                    Cpu.io_time = self.task[self.index + 1]
                    print(f'{self.num}번째 Cpu가 종료하였습니다.')
                    Cpu.exit_count += 1
                    self.status = 2
                else :
                    self.index += 2 
                  
        else :
            Cpu.exit_count +=1
            print(f'{self.num}번째 Cpu가 종료하였습니다.')
            self.status = 2
            
        
            
    def wakeup(self) :
        global time
        
        if time >= self.wait_time and self.status !=2 :
            self.status = 0
            Cpu.wake_count += 1 
            
    

if __name__ == "__main__" :
    
    n = int(input())
    data = [None] * n
    
    for i in range(n) :
        task = list(map(int, sys.stdin.readline().split()))
        data[i] = Cpu(task)
    num = 0
    waste_time = 0
    while True :
        num = 0
        while num < n :
            
            if data[num].status == 0 :
                data[num].tasking()
                for i in range(n) :
                    data[i].wakeup()
                if Cpu.wake_count >= 1 :
                    num = 0 
                    Cpu.wake_count = 0
                    continue
            num += 1
        
        if Cpu.exit_count == n :
            time += Cpu.io_time
            break
        
        if Cpu.wake_count == 0 :
            time += 1
            waste_time += 1
            print(f'낭비된 시간은 {waste_time}입니다.')
            
            for i in range(n) :
                data[i].wakeup()
            Cpu.wake_count = 0
    
    print(time, waste_time)
                
        
        
            
        