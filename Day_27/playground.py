""" *args AKA Many Positional arguments"""


def add(*args):
    sum_total = 0
    for num in args:
        sum_total = num + sum_total
    return sum_total


print(add(2, 3, 4, 5, 6))

""" **Kwargs AKa Key world arguments"""
# def calculate(n, **kwargs)
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=3, multipy=5)

"""Create a class with a lot of keyword arguments"""
class Car:
    def __init__(self, **kw):
        self.model = kw.get("model")
        self.make = kw.get("make")
        self.seat = kw.get("seat")
        self.color = kw.get("color")

new_car = Car(model="GTR", make="Nissan")
print(new_car.make, new_car.model, new_car.seat)