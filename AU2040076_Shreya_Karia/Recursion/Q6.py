#Shreya Karia AU2040076
def HCF(x,y):
    if x%1 != 0 or y%1 != 0 :
        return "Enter a whole number."
    if y == 0 :
        return x
    else:
        if (x%y==0):
            return y
        else:
            return HCF(y,x%y)
        


print(HCF(25,120))
