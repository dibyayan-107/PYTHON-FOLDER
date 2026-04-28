row = int(input("Enter row number : "))
num = 1
for i in range(1, row + 1):
    print()
    for j in range(1, i + 1):
        print(f"{num}", end = ' ')
        num += 1