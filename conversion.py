n = int(input("Enter any number : "))
print(f"{"|----Decimal----|" : <4}{"-----Octal-----|" : <5}{"----Binary----|" : <5}")
for j in range(1, n + 1):
       x = j
       y = j
       val1 = ""
       while j != 0: 
           rem = j % 8
           val1 = val1 + str(rem)
           j = j // 8
           
       val2 = ""
       while x != 0: 
           rem = x % 2
           val2 = val2 + str(rem)
           x = x // 2 
       print(f"\t{y : <5}\t\t{val1[:: -1] : <5}\t\t{val2[:: -1] : <5}")