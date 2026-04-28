num = int(input("Enter a value : "))
str_name = str(num)
rev_str = str_name[: : -1]
if str_name == rev_str:
    print(f"{num} is palindrome number👍:")
else:
    print(f"{num} is not palindrome number 🤦‍♂️.")