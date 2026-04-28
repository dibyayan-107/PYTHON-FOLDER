''' 
Enter row number between 1 to 9 to create Palindromic Triangle using recursion
>> 1
>> 121
>> 12321
>> 1234321
>> 123454321

'''
def f(x):
   if x == 0:
      return 0
   else:
      return 10**(x - 1) + f(x - 1)

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
    a = f(i)
    print(a**2)