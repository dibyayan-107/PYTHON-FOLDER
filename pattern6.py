num = int(input("Enter half row number : "))
for i in reversed(range(1, num + 1)):
    print()
    for j in range(1, i + 1):
        print(" ", end = '')
    for k in range(i, num + 1):
        print("*", end = ' ')
for i in range(1, num):
    print()
    for j in range(1, i + 2):
        print(" ", end = '')
    for k in range(i, num):
        print("*", end = ' ')