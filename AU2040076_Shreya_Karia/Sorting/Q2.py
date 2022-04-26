#Shreya Karia AU2040076
import random

def partition(start,end,array):
    pivot_index = start
    pivot = array[pivot_index]
    print("p",pivot_index,pivot)
    while start<end:
        while array[start] < pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if start<end :
            array[start], array[end] = array[end], array[start]
        if pivot_index == start:
            pivot_index = end
        elif pivot_index == end:
            pivot_index = start
        
    print(array,start,end)
    return pivot_index

def partitionr(start,end,array):
    r_pivot = random.randrange(start,end)
    array[start], array[r_pivot] = array[r_pivot], array[start]
    return partition(start,end,array)

def quicksort_r(start,end,array):
    print(start,end)
    if start<end:
        p = partitionr(start,end,array)
        quicksort_r(start,p-1,array)
        quicksort_r(p+1,end,array)

m = [7,23,12,11,34,56]
quicksort_r(0,len(m)-1,m)
print(m)