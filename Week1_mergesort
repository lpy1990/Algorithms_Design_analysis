'''
Merge and sort

@author: pengyu
'''

def merge_sort(lst):
    if len(lst) <=1:
        return lst
    else:
        mid = len(lst)//2
        x = merge_sort(lst[:mid])
        y = merge_sort(lst[mid:])
         
        return merge(x,y)
     



def merge(a,b):
    i,j = 0,0
    merged = []
     
    while i < len(a) and j< len(b):
        
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
             
    while i< len(a):
        merged.append(a[i])
        i +=1
         
    while j< len(b):
        merged.append(b[j])
        j +=1
         
    return merged

#test cases
print merge_sort([1,45,6,7,25,89,9,76,39,63,86,37])
print merge_sort([2,3,1])


        
