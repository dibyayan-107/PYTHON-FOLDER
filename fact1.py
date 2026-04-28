num = int(input("Enter any number : "))
temp = num
fact = 1
for i in range(1, temp + 1):
    fact = fact * i
print(f"Factorial of {num} : {fact}")
    