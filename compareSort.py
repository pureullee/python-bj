
import random
import time
import pandas as pd 
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(1000000)    
sortSize = 400


def selectionSort(A : list, n : int) :
    if n>0 :
        m = min(A[0:n])
        A.remove(m)
        A.append(m)
        selectionSort(A,n-1)
        


def bubbleSort(A : list, n : int) :
    
    if n>1 :
        for i in range(n-1) :
            if A[i] > A[i+1] :
                A[i], A[i+1] = A[i+1], A[i]
                
        bubbleSort(A, n-1)
        


def insertSort(A : list, start : int , end : int) :
    
    value = A[start] 
    loc = start - 1
    while loc>=0 and A[loc] >= value :
        A[loc+1] = A[loc]
        loc -= 1
        
    A[loc+1] = value
    
    if start + 1 < end : insertSort(A, start+1, end)
    
def compareSort(*args) : # args[0]은 args[1]에 쓰일 함수에 대해 각 시행에 대한 runtime이 들어감. args[1]은 정렬 함수. args[2:]는 정렬 함수에 대한 정렬 리스트를 제외한 매개변수
    for i in range(1000) :
        random.seed(random.randint(0,1000000))
        ls =[random.randint(0,100) for x in range(sortSize)]
        start = time.time()
        args[1](ls, *args[2:])
        end = time.time()
        args[0].append((end-start)) 
        ls = []
        




def run() : 
    df = pd.DataFrame()
    s = []
    compareSort(s,selectionSort,sortSize)
    df['selectionSort'] = s
    s = []
    print('완료')

    compareSort(s,bubbleSort,sortSize)
    df['bubbleSort'] = s
    s = []

    compareSort(s,insertSort,0,sortSize)
    df['insertSort'] = s
    s = []


    print(df.head())
    df.plot(kind='box')

    plt.show()


ls = [8,2,5,7,6,3]
selectionSort(ls,len(ls))
print(ls)
ls = [8,2,5,7,6,3]
bubbleSort(ls,len(ls))
print(ls)
ls = [8,2,5,7,6,3]
insertSort(ls,0,len(ls))
print(ls)

    


  


    


    

    

        
    
    
    
            
            
    