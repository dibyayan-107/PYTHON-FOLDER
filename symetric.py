num = int(input("Enter any number(4 or 6 digit) : "))
sum1 = 0
sum2 = 0
count = 1
temp1 = num
while temp1 > 0:
    r2 = temp1 % 10
    sum2 = sum2 + r2
    temp1 = temp1 // 10
temp2 = num
while count < 3 :
    r1 = temp2 % 10
    sum1 = sum1 + r1
    temp2 = temp2 // 10
    count += 1
if sum2 == sum1 * 2:
    print(f"{num} is a symetric number")
else:
    print(f"{num} is not a symetric number")
