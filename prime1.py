val = int(input("Enter a number to check prime or not : "))
count = 0
for i in range(2, val + 1):
    if val % i == 0:
        count += 1
    else:
        continue
if count == 1:
    print(f"{val} is a prime number  🙂")
else:
    print(f"{val} is not a prime number🙁")