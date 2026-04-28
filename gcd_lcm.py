#GCD & LCM  
def fgcd(n1, n2):
    while n1 != 0:
        rem = n2 % n1
        n2 = n1
        n1 = rem
    return n2
def flcm(n1, n2):
    a = n1 * n2
    while n1 != 0:
        rem = n2 % n1
        n2 = n1
        n1 = rem
    l = a // n2
    return l 
#user input 
D1 = int(input("Enter divisor : "))
D2 = int(input("Enter dividend : "))
if D1 > D2:
    D1, D2 = D2, D1
print(f"G.C.D : {fgcd(D1, D2)}")
print(f"L.C.M : {flcm(D1, D2)}")
    