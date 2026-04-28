txt = str(input("Enter string : "))
w = x = y = z = 0
for i in txt:
   if (i =='a' or i =='e' or i =='i' or i =='o' or i =='u'or
    i =='A' or i =='E' or i =='I' or i =='O' or i =='U'):
        w += 1
   elif i == ' ':
        x += 1
   elif i.isdigit():
        y += 1
   else:
        z += 1
print(f"The number of vowels : {w}")
print(f"The number of consonants : {z}")
print(f"The number of white spaces: {x}")      
print(f"The number of digits : {y}")