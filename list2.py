#checking prime number or composite number
flag = 0
n = int(input("Enter any number : "))
if n <= 1:
    print(f"{n} is nether prime or composite number!!")
    exit(0)
temp = n
for i in range(2, temp + 1):
    if temp % i == 0:
        flag += 1
    if flag > 1:
        break
if flag == 1:
    print(f"{n} is a prime number!!")
else:
    print(f"{n} is a composite number!!")