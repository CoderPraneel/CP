def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
def nCr(n,r,m):
    return((factorial(n)//factorial(n-r))%m)
n=int(input("enter value of n: "))
r=int(input("enter value of r: "))
m=int(input("enter value of m: "))
print("nCr % m is",nCr(n,r,m))
