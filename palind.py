num = int(input("Enter any positive integer:"))
rev = 0
temp = num
while temp > 0:
    
    rem = temp % 10
    rev = rev*10 + rem
    temp = temp // 10

if rev == num:
    print("%d is palindrome number" %num)
else:
    print("%d is not palindrome number" %num)
    