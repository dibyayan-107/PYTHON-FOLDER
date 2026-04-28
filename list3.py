#Performing some basic operation in list
#user input
list1 = []
N = int(input("How many times you want to execute>> "))
for x in range(N):
    print("1.insert\n2.print\n3.remove\n4.append\n5.sort\n6.pop\n7.reverse")
    n = int(input("Enter your choice : "))
    match n:
        case 1:
            index = int(input("Enter index : "))
            val = int(input("Enter value : "))
            list1.insert(index, val)
            break
        case 2:
            print(">>",list1)
            break
        case 3:
            num = int(input("Enter value : "))
            list1.remove(num)
            break
        case 4:
            val = int(input("Enter value : "))
            list1.append(val)
            break
        case 5:
            list1.sort()
            break
        case 6:
            index = int(input("Enter index : "))
            list1.pop(index)
        case 7:
            list1.reverse()
            break
        case _:
            print("Invalid choice!!")
            break