#Converting string into toggle case
original_string = input("Enter string : ")
new_string = ""
for ch in original_string:
    if ch.islower():
        new_string += ch.upper()
    elif ch.isupper():
        new_string += ch.lower()
    else:
        new_string += ch
original_string = new_string
print(original_string)