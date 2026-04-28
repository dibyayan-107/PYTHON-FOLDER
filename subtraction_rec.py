# Subtraction using recursion
def sub(m1, m2):
    if m2 == 0:
        return m1
    else:
        return sub(m1, m2 - 1) - 1
#user input
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(f"Subtraction : {sub(n1, n2)}")