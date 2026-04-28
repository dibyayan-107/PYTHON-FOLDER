val = int(input("Enter the range : "))
print(f"Perfect square integer from 1 to {val}>>")
for i in range(1, val + 1):
    for j in range(1, i + 1):
        if i == pow(j, 2):
            print(f"{i}")
        else:
            pass
