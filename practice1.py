my_list = []
n = int(input("How many student? -> "))
for _ in range(n):
    s = input("Enter Student name :- ")
    c = input("Enter Class :- ")
    m = int(input("Enter total percentage :- "))
    print("--------")
    my_list.append([s, c, m])
print(f"  NAME  | CLASS | PERCENTAGE")    
for i in range(n):
    print(f"{my_list[i][0] : >5}   {my_list[i][1] : >5}    {my_list[i][2] : >5}")