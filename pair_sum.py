my_list = []
n = 0
try:
  n = int(input("Enter how many number you want to add?->"))
except ValueError:
    print("Please enter integer value!!")
    exit()
while n != 0:
    n -= 1
    item = int(input("Enter value : "))
    my_list.append(item)
    
x = len(my_list)
val = int(input("Enter any value : "))
for i in range(x - 1):
    for j in range(i + 1, x):
        if val == my_list[i] + my_list[j]:
            print(f"{val} is a pair value of {my_list[i]} and {my_list[j]}")
            exit()
        else:
            continue
print(f"{val} is not a pair value!!")