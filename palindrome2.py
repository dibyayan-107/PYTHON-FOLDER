# Checking palindrome number
n = int(input("Enter any number : "))
x = str(n)
var = x[: : -1]
if x == var:
    print(f"{n} is a palindrome number!!")
else:
    print(f"{n} is not a palindrome number!!")