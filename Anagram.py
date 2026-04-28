#Anagram checker
s1 = input("Enter first string : ")
s2 = input("Enter second string : ")

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

n = len(s1)
if n == len(s2):
    for item in s1:
        if item in s2 and (s1.count(item) == s2.count(item)):
            continue
        else:
            print("Two strings are not anagrams!!")
            exit()
else: 
    print("Two strings are not anagrams!!")
    exit()
print("Congrats!!Two strings are anagrams!!")