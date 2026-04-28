mylist = []
n = int(input("How many items you want to add? --> "))
for i in range(n):
  value = (input(f"\nEnter item at [{i}]index : "  ))
  mylist.append(value)
print(mylist)
c = mylist.copy()
c.reverse()
if mylist == c:
    print("It is a palindrome list!!")
else:
    print("It is not a palindrome list")