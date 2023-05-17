
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
               
        
def mergeSort(A : list, start, end) :
    if end - start >= 1 : 
        pc = (start+end)//2
        mergeSort(A,start,pc)
        mergeSort(A,pc+1,end)
        merge(A,start,pc,end)
        
def merge(A,start,pc,end) :
    tmp = [None for x in range(end-start+1)]
    li = start
    ri = pc+1
    idx = 0
    while li<=pc and ri<=end :
        if A[li] < A[ri] : 
            tmp[idx] = A[li]
            li+=1
        else : 
            tmp[idx] = A[ri]
            ri+=1
        idx+=1
    if ri>end :
        for i in range(li,pc+1) :
            tmp[idx] = A[i]
            idx+=1
            
            
    elif li>pc :
        for i in range(ri,end+1):
            tmp[idx] = A[i]
            idx+=1
            
    idx = 0 
    for i in range(start,end+1) :
        A[i] = tmp[idx]
        idx+=1
        
def quickSort(A : list, p, r) :
    if p < r :
        pivotIndex = partition(A, p, r)
        quickSort(A, p, pivotIndex-1)
        quickSort(A, pivotIndex+1, r)
        
def partition(A : list, p, r) :
    pivot = A[r]
    i = p
    j = r-1
    while i<=j :
        if A[i] > pivot :
            if A[j] <= pivot :
                A[i], A[j] = A[j], A[i]
                j -=1
                i +=1
            else : 
                j -=1
        else :
            i += 1
    A[r], A[j+1] = A[j+1], A[r]
    return j+1

def percolateDown(A : list, k:int, end:int) : # repair heap
    child = 2*k+1 # left 
    right = 2*k+2 # right
    if child <= end : 
        if right <= end and A[child] < A[right] :
            child = right # select a large value between A[child] A[right]
        if A[k] < A[child] :
            A[k], A[child] = A[child], A[k] # change parent, child
            percolateDown(A, child, end) 
            
def buildHeap(A) :
    for i in range((len(A)-2) // 2, -1,-1): # First parent ~ last parent
        percolateDown(A,i,len(A)-1)
        
def heapSort(A) :
    buildHeap(A)
    for last in range(len(A)-1,0,-1) : 
        A[last], A[0] = A[0], A[last] # A[0],the biggest value, save in A[last] 
        percolateDown(A,0,last-1) # except A[last], 0~last-1 heap
        
def 
        
               
            
    
                     
    

    
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
    
    compareSort(s,mergeSort,0,sortSize-1)
    df['mergeSort'] = s
    s = []
    print('완료')
    
    compareSort(s,quickSort,0,sortSize-1 )
    df['quickSort'] = s
    s = []
    print("완료")
    
    compareSort(s,heapSort)
    df['heapSort'] = s
    s = []
    print("완료")
    
    df.plot(kind='box')  
    plt.show()




