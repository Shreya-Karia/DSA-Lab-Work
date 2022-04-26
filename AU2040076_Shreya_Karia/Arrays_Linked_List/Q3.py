#Shreya Karia AU2040076

def delatind(arr,pos):
    for i in range(0,len(arr)+1):
        if pos>len(arr):
            return "Enter position in range."
        if (i + 1) == pos:
            return arr[:i] +arr[i+1:]


arr = [23,4,5,67,8]
delatind(arr,3)
print(arr)