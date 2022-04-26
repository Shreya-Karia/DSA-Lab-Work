#Shreya Karia AU2040076
def prodArray(arr):
    if len(arr) == 0:
        return 1
    return arr[len(arr)-1] * prodArray(arr[:-1])

a = prodArray([1,4,5,6])
print(a)
    