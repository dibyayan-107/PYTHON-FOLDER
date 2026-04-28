#Checking palindrome string using recursion
def reverse(str2):
    if len(str2) <= 1:
        return str2
    else:
        return str2[-1] + reverse(str2[: -1])
#user input
str1 = input("Enter a string : ")
is_check = bool(str1 == reverse(str1))
if is_check:
    print("The string is palindrome!!!")
else:
    print("The string is not palindrome!!!")