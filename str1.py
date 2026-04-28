str = str(input("Enter string : "))
x = 0
y = 0
for i in str:
    if i.isupper():
        x += 1
    elif i.islower():
        y += 1
print("Number of uppercase character :",x)
print("Number of lowercase character :",y)