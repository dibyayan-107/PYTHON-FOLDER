txt = str(input("Enter string : "))
print("All the consonant deleted from the string,\nthen the new string>> ")
for i in range(len(txt)):
    for j in txt:
        if(j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u' 
          or j == 'A' or j == 'E' or j == 'I' or j == 'O' or j == 'U'):
          if txt[i] == j:
            print(f"{j}", end = " ")
            break                      