def prime(x):
    count = 0
    if x <= 1:
        print(f"Invalid Input!!!")
        exit()
    for i in range(2, x + 1):
       if x % i == 0:
        count += 1
    if count == 1:
        print(f"{x} is a prime number !!!")
    else:
        print(f"{x} is not a prime number!!!")

a = int(input("Enter any number : "))
prime(a)