class Person:
    def __init__(self, init_age):
        self.age = init_age
        if self.age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")

    def am_I_Old(self):
        if self.age < 13:
            return "You are Young!!"
        elif 13 <= self.age <= 18:
            return "You are a Teenager!!"
        else:
            return "You are Old!!"

    def year_passes(self):
        self.age += 3
        return self.age

try:
    age = int(input("Enter age : "))
except ValueError as x:
    print("Error code :- ",x)
    exit()
p1 = Person(age)
print("Current state> ",p1.am_I_Old())
p1.year_passes()
print("After 3 years> ", p1.am_I_Old())