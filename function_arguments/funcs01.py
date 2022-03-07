# parameter passing : start
# pass by value or reference
# also known in python pass by object or object reference

def foo(x):
    x = 5  # x is a local variable here


var = 10
foo(var)
print(var)


def foo2(my_list):
    my_list.append(4)


my_list = []
foo2(my_list)
print(my_list)  # my_list would be modified since it was passed as reference to foo2
# mutable objects can't be changed
# immutable objects can't be changed
# mutable object contain within immutable objecs can be changed


def foo3(a_list):
    # here we create a new local reference and assigned to a_list, this doesn't modified the a_list variable outside of the function
    a_list = [200, 300, 400]
    a_list.append(4)
    a_list[0] = -100


a_list = [1, 2, 3]
foo3(a_list)
print(a_list)  # would print [1, 2, 3]


# parameter passing : end
