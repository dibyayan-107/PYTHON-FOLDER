num = int(input("Enter a number : "))
count = 0
for i in range(1, num):
    if(num == pow(i, 2)):
        count += 1
    else:
        pass
if(count == 1):
    print(f"{num} is perfect square integer(^_^)")
else:
    print(f"{num} is not perfect square integer(T_T)")
