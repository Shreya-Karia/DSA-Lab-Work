#Shreya Karia AU2040076
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n%1 != 0 :
        return "Enter a whole number."
    if n < 0:
        return "Enter a positive integer."
    return fib(n-1) + fib(n-2)

print(fib(4))