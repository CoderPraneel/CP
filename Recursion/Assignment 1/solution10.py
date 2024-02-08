def length(s):
    if s == "":
        return 0
    else:
        return 1 + length(s[1:])
s = str(input("Enter the string: "))
length = length(s)
print("Length of the string:", length)
