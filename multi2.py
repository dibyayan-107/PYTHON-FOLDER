#multiplication using recursion(PART 2)
def multi(l1, l2):
    if l2 == 0:
        return 0
    else:
        return l1 + multi(l1, l2 - 1)
#user input
n1 = int(input("Enter first value : "))
n2 = int(input("Enter second value : "))
print(f"Result : {multi(n1, n2)}")