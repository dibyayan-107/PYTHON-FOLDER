row = int(input("Enter row number : "))
for i in range(1, row + 1):
    print()
    for j in range(i, row + 1):
        print(" ", end = '')
    for k in range(1, i + 1):
        print(f"{i}", end = ' ')