#Shreya Karia AU2040076

def partitionm(start,end,array):
    pivot_index = (start+end)//2
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

def quicksort(start,end,array):
    print(start,end)
    if start<end:
        p = partitionm(start,end,array)
        quicksort(start,p-1,array)
        quicksort(p+1,end,array)



m = [27,12,3,14,56,8,1,25,457,120]
quicksort(0,len(m)-1,m)
print(m)