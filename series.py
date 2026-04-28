n = int(input("Enter the term>>"))
x = int(input("Enter the value>>"))
sum = 0
for i in range(1, n + 1):
    a = (x ** i)/i
    sum = sum + a
print(f"The value of {x}^1/1 + ..... + {x}^{n}/{n} : {sum}")