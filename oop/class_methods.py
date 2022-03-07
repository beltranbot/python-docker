class Person:
    people = 0  # class attribute

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people(cls):
        return cls.people

    @classmethod
    def add_person(cls):
        cls.people += 1



p1 = Person('tim')
p2 = Person('Jill')

print(p2.number_of_people())

print(Person.number_of_people())

