#      *
#    * * *
#  * * * * *
# * * * * * * * 
row_num = int(input("Enter row number : "))
print("Your pyramid is here😎😎>>>\n")
for i in range(1, row_num + 1):
    for j in range(1, (row_num - i) + 1):
        print(" ", end = " ")
    for k in range(1, 2*i):
        if k == 2*i - 1:
            print("*\n")
        else:
            print("*", end = " ")