def fibonacci(n):
    if n <= 0:
        return "Enter a valid number."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter a positive integer (n): "))+1
f_num = fibonacci(n)
print("The Fibonacci number of",n-1,"is:", f_num)