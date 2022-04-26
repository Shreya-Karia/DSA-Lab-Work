#Shreya Karia AU2040076

def srch(arr,el):
    for i in range(0,len(arr)):
        if arr[i] == el:
            return i
        elif i == len(arr) - 1:
            return -1

arr = [23,4,5,67,8]
print(srch(arr,4))