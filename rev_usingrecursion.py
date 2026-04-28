#string reverse using recursion
def rev(s2):
    if len(s2) == 1:
        return s2
    elif s2 == " ":
        return s2
    else:
        return s2[-1] + rev(s2[:-1])
#user input
s1 = input("Enter string : ")
print(f"Original string : {s1}")
print(f"Reversed string : {rev(s1)}")