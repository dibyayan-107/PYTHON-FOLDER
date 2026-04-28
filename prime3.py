def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
a = int(input("Enter any number : "))
if prime(a):
    print(f"{a} is a prime number!!!")
else:
    print(f"{a} is not a prime number!!!")