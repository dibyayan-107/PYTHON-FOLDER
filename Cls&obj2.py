#Average of best of three marks

class average:
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.avg = (self.marks1 + self.marks2 + self.marks3) / 3

    def avg_value(self):
        return self.avg

print(">>Enter best of three marks :- ")
a = int(input("Enter first mark : ")) 
b = int(input("Enter second mark : "))
c = int(input("Enter third mark : "))
s1 = average(a, b, c)
print("Total average : ", s1.avg)