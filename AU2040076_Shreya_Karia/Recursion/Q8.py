#Shreya Karia AU2040076
def reverse(n):
    if len(n) == 0:
        return n
    return reverse(n[1:]) + str(n[0])

print(reverse("Heyyy"))