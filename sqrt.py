import math
sqrt_num = 0
num = int(input("Enter value : "))
if num < 0:
    print("Enter positive value!!!")
    exit
for i in range(1, num + 1):
    if int(math.sqrt(i)) ** 2 == i:
        print(f"Square root of {i} : ",math.sqrt(i))
        sqrt_num += 1
    else:
        continue
print(f"Count : {sqrt_num}")