#Shreya Karia AU2040076

def insatind(arr,pos,el):
    for i in range(0,len(arr)+1):
        if pos>len(arr):
            return "Enter position in range."
        if (i + 1) == pos:
            arr.append(0)
            j = len(arr) -1
            while j> pos-1:
                arr[j] = arr[j-1]
                j = j -1
            arr[i] = el
            return arr

arr = [23,4,5,67,8]
insatind(arr,3,98)
print(arr)