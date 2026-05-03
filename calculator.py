#Basic Calculator

#User input
while True:
    operator = input("Enter operator(+,-,*,/,^) :- ")
    if operator not in ["+", "-", "*", "/", "^"]:
        print("Invalid Operator!")
    else:
        break
while True:
    try:
        n1 = float(input("Enter first value :- "))
        break
    except ValueError:
        print("Invalid value!!")
        
while True:
    try:
        n2 = float(input("Enter second value :- "))
        break
    except ValueError:
        print("Invalid value!!")

# Operation
if operator == "+":
    result = n1 + n2
    print(f"{n1} + {n2} = {result}")

elif operator == "-":
    result = n1 - n2
    print(f"{n1} - {n2} = {result}")

elif operator == "*":
    result = n1 * n2
    print(f"{n1} * {n2} = {result}")

elif operator == "/":
    try:
        result = n1 / n2
        print(f"{n1} / {n2} = {result}")
    except ZeroDivisionError as x:
        print("Error Code : ", x)
    
elif operator == "^":
    result = n1 ** n2
    print(f"{n1} ^ {n2} = {result}")