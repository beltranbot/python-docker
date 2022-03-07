class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')


class Dog(Pet):
    def speak(self):
        print('Bark')


cat = Cat('Garfield', 19, 'orange')
cat.show()
cat.speak()

dog = Dog('Pluto', 10)
dog.show()
dog.speak()
