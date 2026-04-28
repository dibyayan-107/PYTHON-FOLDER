# factorial using tail recursion
def fact(n, p):
    if n == 0:
        return 1
    elif n == 1:
        return p
    else:
        return fact(n - 1, n * p)
#user input
ischeck = 0
while ischeck == False:
    num = int(input("Enter any number : "))
    ischeck = bool(num >= 0)
    if ischeck:
        break
    else:
        print("Please input positive no. to get factorial!!")
print(f"Factorial of {num} : {fact(num, 1)}")