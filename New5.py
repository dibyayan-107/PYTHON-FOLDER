s1 = set()
s2 = {2,6,4,7,0,8,5}
n = int(input("How many items you want to add : "))
while n != 0:
 val = int(input("Enter value : "))
 s1.add(val)
 n -= 1
print(f"Set1 : {s1} and Set2 : {s2}")
print("How many times you want to run? ")
time = int(input())
while time != 0:
 print("1. | for union>")
 print("2. & for intersection>")
 print("3. - for difference>")
 print("4. ^ for symmetric difference>")
 symbol = input("Which operations you want to perform : ")
 match(symbol):
     case '|':
        set3 = s1.union(s2)
        print(f"Result : {set3}")
        continue
     case '&':
        set3 = s1.intersection(s2)
        print(f"Result : {set3}")
        continue
     case '-':
        set3 = s1.difference(s2)
        print(f"Result : {set3}")
        continue
     case '^':
        set3 = s1.symmetric_difference(s2)
        print(f"Result : {set3}")
        continue 
     case _:
       print("Invalid symbol!!!") 
       continue
 time -= 1
