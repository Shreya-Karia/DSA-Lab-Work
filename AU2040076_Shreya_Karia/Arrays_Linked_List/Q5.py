#Shreya Karia AU2040076

def insatbeg(arr,el):
    arr.append(0)
    i = len(arr) - 1
    while i>=0:
        if i != 0:
            arr[i] = arr[i-1]
        else:
            arr[i] = el
        i = i - 1
    return arr
    

arr = [1,2,3,4,5,6]
print(insatbeg(arr,10))