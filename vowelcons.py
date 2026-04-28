ans = input("Enter any word : ")
vcount = 0
ccount = 0
for i in range(len(ans)):
    if(ans[i] == "a" or ans[i] == "e"or ans[i] == "i" or ans[i] == "o"or ans[i] == "u"or
       ans[i] == "A" or ans[i] == "E" or ans[i] == "I" or ans[i] == "O" or ans[i] == "U"):
       vcount += 1
    elif (ans[i] == " "):
        pass
    else:
       ccount += 1
print(f"The number of vowels : {vcount}")
print(f"The number of consonant : {ccount}")