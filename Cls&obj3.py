import math

class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        d = 2*self.radius
        print("Diameter :- ", d)

    def volume(self):
        v = 4/3*math.pi*self.radius**3
        print(f"Volume :- {round(v, 2)}")

    def area(self):
        a = 4*math.pi*self.radius**2
        print(f"Surface area :- {round(a, 2)}")


r1 = int(input("Enter radius for sphere :- "))
s1 = Sphere(r1)
s1.diameter()
s1.area()
s1.volume()

