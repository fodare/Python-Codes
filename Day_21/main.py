"""
Day 21
Class Inheritance and slicing to tuples, lists

"""


class Animal():
    def __int__(self):
        self.eyes = 2

    def breathe(self):
        print(f"Inhale and exhale")
        
        
        
class Dog(Animal):
    def __int__(self):
        super(Dog, self).__int__()

    def sound(self):
        print(f"I'm a dog i bark")

    def print_eyes(self):
        super().eyes
        print(f"I could also have 4 eyes is things go south")

    def run(self):
        print(f"I run on my four legs!")

dogo = Dog()
dogo.sound()


alhaphet = ("a", "b", "c", "d", "e", "f", "g")
sliced_values = alhaphet[2:5] # Print the value from the 2 index value to the value on the 5 index
print(f"Sliced value is")