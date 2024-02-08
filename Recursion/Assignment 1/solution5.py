def eq(a,b):
    if b==1 :
        return a
    else:
        return a*eq(a,b-1)
a=int(input())
b=int(input())
m=int(input())
print(eq(a,b)%m)