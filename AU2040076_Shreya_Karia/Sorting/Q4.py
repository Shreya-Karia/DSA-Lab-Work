#Shreya Karia AU2040076
def hash_table(list,size):
    arr = [0]*size
    l = len(list)
    for j in range(0,l):
        mod1 = list[j]%size
        while arr[mod1] != 0:
            mod1 = (mod1+ 1)%size
        arr[mod1] = list[j]
    return arr

def hash_search(hashtable,value):
    size = len(hashtable)
    mod1 = value%size
    while hashtable[mod1] != 0:
        if hashtable[mod1] == value:
            return True
        mod1 = (mod1+ 1)%size
    return False

 


    

input_hash = [133,88,92,221,174]
a = hash_table(input_hash,17)
print(a)
print(hash_search(a,100))
print(hash_search(a,133))
print(hash_search(a,174))

print(hash_table(input_hash,37))
b = hash_table(input_hash,37)
print(b)
print(hash_search(b,100))
print(hash_search(b,133))
print(hash_search(b,174))




    
    