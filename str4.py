# string reverse without sliceing function
txt = str(input("Enter string : "))
for i in reversed(range(len(txt))):
    print(f"{txt[i]}", end = " ")