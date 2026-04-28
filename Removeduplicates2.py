my_list = []
unique_list = []
n = int(input("How many items you want to add? "))
for i in range(n):
    value = int(input(f"Enter item at index[{i}] : "))
    my_list.append(value)
print(f"Original list : {my_list}")
for item in my_list:
     if my_list.count(item) == 1:
        unique_list.append(item)
print(f"Unique list : {unique_list}")