strg = str(input("Enter string(s) : "))
alpha = digit = space = upper = lower = 0
for i in strg:
    if(i.isalpha()):
        alpha += 1
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
    elif(i.isdigit()):
        digit += 1
    elif(i.isspace()):
        space += 1
print(f"Alphabet : {alpha}\nDigit : {digit}\nSpace : {space}\nUppercase : {upper}\nLowercase : {lower}")