#Shreya Karia AU2040076
def isPali(n):
    if len(n) == 0:
        return True
    if n[0] == n [-1]:
        return isPali(n[1:-1])
    else:
        return False

print(isPali("malayalam"))
