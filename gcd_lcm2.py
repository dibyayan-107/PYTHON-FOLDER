#GCD & LCM using recursion
def fgcd(n1, n2):
    if n1 != 0:
        rem = n2 % n1
        n2 = n1
        n1 = rem
        fgcd(n1, n2)
    else:
        print(f"G.C.D : {n2}")

def flcm(n1, n2, a):
    if n1 != 0:
        rem = n2 % n1
        n2 = n1
        n1 = rem
        flcm(n1, n2, a)
    else:
        l = a // n2
        print(f"L.C.M : {l}")
#user input
D1 = int(input("Enter divisor : "))
D2 = int(input("Enter dividend : "))
a = D1 * D2
if D1 > D2:
    D1, D2 = D2, D1
fgcd(D1, D2)
flcm(D1, D2, a)
