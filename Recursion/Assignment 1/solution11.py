def palindrome(a):
    if len(a) <= 1:
        return 'a is palindrome'
    elif a[0] != a[-1]:
        return 'a is not palindrome'
    else:
        return palindrome(a[1:len(a)-1])
a = str(input('Enter a string: '))
check = palindrome(a)
print(check)
