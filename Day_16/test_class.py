class Person:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def printData(self):
        print(f"Hello my name is {self.name} and i am {self.sex} years old")

contenstant_1 = Person("Damilare", "Male" )
contenstant_1.printData()