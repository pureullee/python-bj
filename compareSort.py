
import random
import time
import pandas as pd 
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(1000000)    
sortSize = 400


def selectionSort(A : list, n : int) :
    if n>0 :
        max_idx = 0 # initial index
        for i in range(1,n) : # except 0
            if A[max_idx] < A[i] : max_idx = i # search index to maximize value
        A[max_idx], A[n-1] = A[n-1], A[max_idx] # swap, A[n-1] > for x in A[0:n-1]
                  
        selectionSort(A,n-1) # recursion
        


def bubbleSort(A : list, n : int) :
    
    if n>1 :
        for i in range(n-1) : # swap count = n-1
            if A[i] > A[i+1] : # swap
                A[i], A[i+1] = A[i+1], A[i]
                
        bubbleSort(A, n-1)
        


def insertSort(A : list, start : int , end : int) :
    
    value = A[start] # save A[start]
    loc = start - 1 # max index A[0:start] 
    while loc>=0 and A[loc] >= value : # shift and to search the right index
        A[loc+1] = A[loc]
        loc -= 1
        
    A[loc+1] = value # insert 
    
    if start + 1 < end : insertSort(A, start+1, end)
    
def compareSort(*args) : # args[0]은 args[1]에 쓰일 함수에 대해 각 시행에 대한 runtime이 들어감. args[1]은 정렬 함수. args[2:]는 정렬 함수에 대한 정렬 리스트를 제외한 매개변수
    for i in range(1000) :
        random.seed(time.time()) # when i call compareSort, to make random list 
        ls = [random.randint(0,100) for x in range(sortSize)] # comprehension
        start = time.time() # estimate run time
        args[1](ls, *args[2:]) # args[1] = func, args[2:] = variable about func
        end = time.time()
        args[0].append((end-start)) # args[0] = save run time data 
        ls = [] # clear
        




def run() : 
    df = pd.DataFrame() 
    s = [] # save run time data 
    compareSort(s,selectionSort,sortSize)
    df['selectionSort'] = s
    s = []
    print('완료')

    compareSort(s,bubbleSort,sortSize)
    df['bubbleSort'] = s
    s = []
    print('완료')

    compareSort(s,insertSort,0,sortSize)
    df['insertSort'] = s
    s = []
    print('완료')

    df.plot(kind='box')

    plt.show()


run()

    


  


    


    

    

        
    
    
    
            
            
    