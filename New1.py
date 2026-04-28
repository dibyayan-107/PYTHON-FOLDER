# Write a program in python to count the frequency of all the elements of a given tuple. 
list1 = []
num = int(input("How many elements you want to add?---> "))
for i in range(0, num):
    val = int(input(f"Enter elememt at index[{i}]: "))
    list1.append(val)
my_tuple = tuple(list1)
print(f"Your tuple : {my_tuple}")
for i in my_tuple:
    count = 0
    for j in my_tuple:
        if i == j: 
            count += 1
        else:
            continue
    print(f"Frequency of {i} : {count}")
    