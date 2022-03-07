import secrets

a = secrets.randbelow(10) # from 0 to 10, not including 10
print(a)

a = secrets.randbits(4) # 0000 - 1111
print(a)

mylist = list("ABCDEFGH")
a = secrets.choice(mylist) # non repoducible chioces
print(a)
