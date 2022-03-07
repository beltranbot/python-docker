import random

a = random.random() # Get the next random number in the range [0.0, 1.0)
print(a)

b = random.uniform(1, 10)
print(b) # Get a random number in the range [a, b) or [a, b] depending on rounding.

c = random.randint(1, 10) # Return random integer in range [a, b], including both end points.
print(c)

d = random.randrange(1, 10) # doesn't include the endpoint
print(d)

e = random.normalvariate(0, 1) # mu, sigma: mean of 0, standard deviation of 1
print(e)

mylist = list("ABCDEFGH")
a = random.choice(mylist) # random element of the list
print(a)

a = random.sample(mylist, 3) #randomly pick 3 elements of the list, not duplicated
print(a)

a = random.choices(mylist, k=3) # randomly pick 3 elements, can be duplicated
print(a)

random.shuffle(mylist) # shuffle list
print(mylist)

# get the same random values every tiem
random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))
