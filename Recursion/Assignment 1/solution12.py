def digit_sum(n):
    if n=='':
        return 0
    else:
        return int(n[0]) + digit_sum(n[1:])
n=str(input("Enter a number:"))
print("The digit sum is",digit_sum(n))
