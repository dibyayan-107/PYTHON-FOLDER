#Recreating an integer list into a special list which have no duplicates
list1 = []
unique_list = []
n = int(input("How many items you want to add>> "))
while n:
    val = int(input("Enter item : "))
    list1.append(val)
    n -= 1
print("Old list : ",list1)
for x in list1:
    num = list1.count(x)
    if num > 1:
        if x not in unique_list:
            unique_list.append(x)
        else:
            continue
    else:
        unique_list.append(x)
list1 = unique_list.copy()
list1.sort()
print("New list : ",list1)
str1 = "".join(str(x) for x in list1)
print("Converted into String : ",str1)