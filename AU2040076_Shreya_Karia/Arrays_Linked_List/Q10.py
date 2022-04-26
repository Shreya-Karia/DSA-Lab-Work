#Shreya Karia AU2040076
def replatind(arr,i,el):
    if(1<=i<=len(arr)):
        arr[i]= el
        return arr
    else:
        return -1

print(replatind([1,2,3,4,5,19,20],4,6))