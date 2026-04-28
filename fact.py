num = int(input("Enter any number : "))
fact = 1
temp = num
while temp > 0:
    fact = fact*temp
    temp-= 1
print(f"{fact} is a factorial of {num}")
