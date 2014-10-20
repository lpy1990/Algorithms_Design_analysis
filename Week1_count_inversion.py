'''
Algorithms - design and analysis (Stanford)
assigenment1


@author: pengyu
'''

def sort_and_count(lst):
    if len(lst) <=1:
        return lst,0
    else:
        mid = len(lst)//2
        x,x_count = sort_and_count(lst[:mid])
        y, y_count= sort_and_count(lst[mid:])
        z,split_count= count_split_inv(x,y)
        return z, x_count+ y_count+ split_count
     



def count_split_inv(a,b):
    counter,i,j = 0,0,0
    
    merged = []
     
    while i < len(a) and j< len(b):
        
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            counter += len(a[i:])
            j += 1
             
    while i< len(a):
        merged.append(a[i])
        i +=1
         
    while j< len(b):
        merged.append(b[j])
        j +=1
         
    return  merged, counter

#test cases
print sort_and_count([1,45,6,7,25,89,9,76,39,63,86,37])
print sort_and_count([2,3,1])

f = open('IntegerArray.txt','r')
lst = []
line = f.readline()
while line != '':
    lst.append(int(line))
    line = f.readline()
    
    
print (sort_and_count(lst))


        
