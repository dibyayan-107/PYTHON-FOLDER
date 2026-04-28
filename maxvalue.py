a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))
if a > b:
    if a > c:
        print("%d is larger than %d and %d." %(a,b,c))
    else:
        print("%d is larger than %d and %d" %(c,a,b))
elif b > a:
    if b > c:
        print("%d is larger than %d and %d." %(b,a,c))
    else:
        print("%d is larger than %d and %d" %(c,a,b))