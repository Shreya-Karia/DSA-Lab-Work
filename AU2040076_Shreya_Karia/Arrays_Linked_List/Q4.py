#Shreya Karia AU2040076

def insatend(arr,el):
    arr.append(0)
    arr[len(arr)-1] = el
    return arr

arr = [1,2,3,4,5,6]
print(insatend(arr,10))