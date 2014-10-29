'''


@author: pengyu
'''
comparision = 0
pivot_model = 2
def quick_sort(a, left, right):
    if len(a) <= 1:
        return a 
    
    if left< right:
        pivot = partition(a, left, right)
        quick_sort(a, left, pivot -1)
        quick_sort(a, pivot+1, right)
        
        
        
        
def partition(a, left, right):
    global comparision
    pivotindex = choose_pivot(a,left,right)
    pivot = a[pivotindex]
    
    #put pivot into the last position of the list
    
    i = left + 1
    for j in range(left+1, right+1):#####j is from left+1 to right, but use range(left+1,right+1)!!
        if a[j] <= pivot:            
            swap(a, j, i)
            i += 1
    swap(a, left, i-1)
    comparision += (right -left)
    return i-1

def is_median(a, i, j, k):

    return (a[i] < a[j] and a[i] > a[k]) or\
           (a[i] > a[j] and a[i] < a[k])


def swap (a,x,y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp
    
def quicksort(alist):
    return quick_sort(alist, 0, len(alist)-1)

def choose_pivot(a,left,right):
    if pivot_model ==0:
        return left
    elif pivot_model == 1:
        swap(a,left,right)  # set the right one as pivot and change position with left one and pivot
        return left
    elif pivot_model == 2:
        mid = left + ((right - left + 1) // 2)
        if ((right - left + 1) % 2 == 0):
            mid -= 1 # Per assignment instructions
        if is_median(a, left, mid, right):
            return left
        elif is_median(a, mid, left, right):
            
            swap(a, left, mid)
            return left
        else:
            
            swap(a, left, right)
            return left
        

#print quicksort([3,4,5,2])

f = open('QuickSort.txt','r')
lst = []
line = f.readline()
while line != '':
    lst.append(int(line))
    line = f.readline()
      
      
print (quicksort(lst))
print comparision
