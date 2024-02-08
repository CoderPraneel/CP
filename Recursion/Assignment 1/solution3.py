def rev(s):
    if len(s) == 0:
        return s
    else:
        return rev(s[1:]) + s[0]
s = input("Enter the string: ")
print("initial string:", s)
print("final string:", rev(s))
