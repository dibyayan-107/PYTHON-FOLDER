# * * * * * * *
#   * * * * *
#     * * * 
#       *  
row_num = int(input("Enter row number: "))
for i in reversed(range(1, row_num + 1)):
    for j in range(i, row_num + 1):
        print(" ", end = " ")
    for k in range(1, 2*i):
        if k == 2*i - 1:
            print("*\n")
        else:
            print("*", end = " ")