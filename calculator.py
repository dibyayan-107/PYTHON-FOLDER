#Basic Calculator

#User input
operator = input("Enter operator(+,-,*,/,^) : ")
while True:
    try:
        n1 = int(input("Enter first value :- "))
        break
    except ValueError:
        print("Please enter integer value!!")
        
while True:
    try:
        n2 = int(input("Enter first value :- "))
        break
    except ValueError:
        print("Please enter integer value!!")

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
else:
    print(f"{operator} is invalid operator😐")