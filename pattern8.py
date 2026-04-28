''' 
Enter row number between 1 to 9 to create Palindromic Triangle 
>> 1
>> 121
>> 12321
>> 1234321
>> 123454321

'''
try:
    while True:
      n = int(input("Enter row number : "))
      if n > 9:
        print("Invalid row number!!")
      else:
         break
except ValueError as a:
    print("Error code : ",a)
    exit()

for i in range(1, n + 1):
   x = (10**i - 1) // 9
   print(pow(x, 2))
    