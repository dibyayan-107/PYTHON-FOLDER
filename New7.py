# A simple calculator using lambda function
adder = lambda x, y: x + y
sub = lambda x, y: x - y
multi = lambda x, y: x * y
div = lambda x, y: x / y

val1 = float(input("Enter first value : "))
val2 = float(input("Enter second value : "))
operator = input("Select Operator(+, -, *, /) :- ")
if operator == '+':
    print("Addition : ", adder(val1, val2))
elif operator == '-':
    print("Subtraction : ", sub(val1, val2))
elif operator == '*':
    print("Multiplication : ", multi(val1, val2))
elif operator == '/':
    print("Division : ", div(val1, val2))
else:
    print("Invalid operator!!")