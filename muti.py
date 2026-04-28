# multiplication using recursion(PART 1 )
def multi(num1, num2, c):
    if c == 2:
       return 1
    else:
       c += 1
       return num1*multi(num2, num1, c)
#user input
count = 0
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(f"Result : {multi(n1, n2, count)}")