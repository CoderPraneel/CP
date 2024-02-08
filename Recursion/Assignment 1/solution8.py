def bin(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return bin(n // 2) + str(n % 2)
num = int(input("Enter the number: "))
binary= bin(num)
print("the binary of",num,"is",binary)
