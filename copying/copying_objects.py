import copy

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass


class Company:

    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee



p1 = Person('Alex', 27)
p2 = p1

p2.age = 28

print(p1.age) # both objects are affected
print(p2.age) 

boss = Person('Alex', 50)
employee = Person('Joe', 26)

company = Company(boss, employee)
company_copy = copy.copy(company) # shallow copy

company_copy.boss.age = 51

print(company_copy.boss.age)
print(company.boss.age)


# deep copying
boss = Person('Alex', 50)
employee = Person('Joe', 26)

company = Company(boss, employee)
company_copy = copy.deepcopy(company) # deep copying

company_copy.boss.age = 51

print(company_copy.boss.age)
print(company.boss.age)
