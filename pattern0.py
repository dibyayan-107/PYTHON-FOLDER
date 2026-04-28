n = int(input("Enter row number>> "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 == 0:
            if j == i:
                print("0\n")
            else:
                print("0", end = " ")
        elif j % 2 != 0:
            if j == i:
                print("1\n")
            else:
                print("1", end = " ")