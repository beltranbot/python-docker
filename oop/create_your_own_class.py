class Dog:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print('Bark')


d = Dog("")
print(type(d))  # prints module and class <class '__main__.Dog'>
d.bark()
print(d.add_one(3))


d = Dog("Tim", 2)
print(d.name)
print(d.get_name())
d2 = Dog("bill", 3)
print(d2.name)
print(d2.get_name())
