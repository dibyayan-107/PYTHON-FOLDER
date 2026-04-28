#Enter a list to check it is palindrome or not
import cyberclip as x
old_list = list(input("Enter a list>> "))
x.copy(old_list.reverse())
new_list = x.paste()
if new_list == old_list:
    print("The list is pailindrome")
else:
    print("The list is not palindrome")