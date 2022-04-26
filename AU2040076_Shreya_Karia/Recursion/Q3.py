#Shreya Karia AU2040076
def addup(n):
    if(n==0):
        return 0
    return n + addup(n-1)
num = int(input("Enter a number: "))
print("Sum :",addup(num))

 
