a = int(input("Enter first value : "))
b = int(input("Enter second value : "))
c = 0
operator = input("Enter any bitwise operater>>")
if operator == '&':
    print("SO, you want to do bitwise AND operation!")
    c = a & b
    print(f"Value in decimal : {c}\nValue in binary : {bin(c)}")
elif operator == '|':
    print("SO, you want to do bitwise OR operation!")
    c = a | b
    print(f"Value in decimal : {c}\nValue in binary : {bin(c)}")
elif operator == '^':
    print("SO, you want to do bitwise XOR operation!")
    c = a ^ b
    print(f"Value in decimal : {c}\nValue in binary : {bin(c)}")
elif operator == '~':
    choice = int(input("On which number you want to do 1's compliment??"))
    if choice == a:
        c = ~a
        print(f"Value in decimal : {c}\nValue in binary : {bin(c)}") 
    else:
        c = ~b
        print(f"Value in decimal : {c}\nValue in binary : {bin(c)}")
else:
    print("Invalid operator!!!😐")