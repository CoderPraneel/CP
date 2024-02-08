def rmv(s):
    if len(s) <= 1:
        return s
    else:
        if s[0] == s[1]:
            return rmv(s[1:])
        else:
            return s[0] + rmv(s[1:])
s = input("Enter a string: ")
new_string = rmv(s)
print("New string is", new_string)
