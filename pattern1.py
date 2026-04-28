# *
# * *
# * * *
# * * * *
# * * * * *
row_num = int(input("Enter row number : "))
for i in range(1, row_num + 1):
    for j in range(1, i + 1):
        if i == j:
            print("*\n")
        else:
            print("*", end = " ")    
