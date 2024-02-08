def count_occurrences(arr, num, index):
    if index == len(arr):
        return 0
    else:
        if arr[index] == num:
            return 1 + count_occurrences(arr, num, index + 1)
        else:
            return count_occurrences(arr, num, index + 1)

arr = [int(x) for x in input("Enter the elements of the list separated by space: ").split()]
num = int(input("Enter the number to count occurrences: "))
count = count_occurrences(arr, num, 0)
print("Total occurrences of", num, "in the array:", count)
