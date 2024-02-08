def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
if a < b:
    a, b = b, a
final = gcd(a, b)
print("The Greatest common divisor (GCD) of", a, "and", b, "is:", final)
