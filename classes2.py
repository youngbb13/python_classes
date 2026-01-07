class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old!")

p1 = Person("Dima", 20)
p1.greet()


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"{self.brand} {self.model} {self.year}")

car1 = Car("Mercedes", "E200", 1998)
car1.display_info()