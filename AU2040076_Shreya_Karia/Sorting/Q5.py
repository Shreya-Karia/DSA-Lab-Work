#Shreya Karia AU2040076
def hash_table_bit(list,size1,size2):
    arr1 = [0]*size1
    l = len(list)
    for j in range(0,l):
        mod1 = list[j]%size1
        arr1[mod1] = 1
    arr2 = [0]*size2
    for j in range(0,l):
        mod1 = list[j]%size2
        arr2[mod1] = 1
    return arr1,arr2   
def hash_search_bit(hashtable1,hashtable2,value):
    size1 = len(hashtable1)
    mod1 = value%size1
    size2 = len(hashtable2)
    mod2 = value%size2
    if hashtable2[mod2] == 1 and hashtable1[mod1] == 1:
        return True
    else:
        return False
        
    
    

input_hash = [133,88,92,221,174]
c,d = hash_table_bit(input_hash,17,37)
print(c,d)
print(hash_search_bit(c,d,100))
print(hash_search_bit(c,d,133))
print(hash_search_bit(c,d,174))
print(hash_search_bit(c,d,170))



    