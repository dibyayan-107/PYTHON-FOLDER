#Finding occurences of a particular character in string
my_str = input("Enter string : ")
unique_list = []
for x in my_str:
    n = my_str.count(x)
    if n > 1:
        if x not in unique_list:
            unique_list.append(x)
        else:
            continue
    else:
        unique_list.append(x)
        
print(f"All Occurences>> ")
for item in unique_list:
    if item == " ":
        continue
    n = my_str.count(item)
    print(f"{item} : {n}")