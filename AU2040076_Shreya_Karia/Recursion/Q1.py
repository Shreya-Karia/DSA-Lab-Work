#Shreya Karia AU2040076
def factorial(num):
    if num == 0 or num == 1 :
        return 1
    if num%1 != 0 :
        return "Enter a whole number."
    if num < 0:
        return "Enter a positive integer."
    return num * factorial(num - 1)

print(factorial(5))
