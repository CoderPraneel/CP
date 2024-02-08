def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")
n = int(input("Enter a number: "))
if n <= 0:
    print("enter a valid number.")
else:
    print_numbers(n)