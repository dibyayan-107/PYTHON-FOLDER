#Write a program in python to calculate the mean of elements of a given list of integers.
My_list = []
i = 0
while True:
    val = input(f"Enter item at index[{i}] : ")
    if val == ' ':
        break
    try:
        val = float(val)
        My_list.append(val)
        i += 1
    except ValueError:
        print("Invalid input, please try again")
        exit()
print(f"Your List : {My_list}")
sum = 0
for i in My_list:
    sum += i
mean = sum / len(My_list)
print(f"The mean of elements : {mean}")
