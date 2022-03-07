# app.py
import json
# # convert dict to json
# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "hasChildren": False,
#     "titles": ["engineer", "programmer"]
# }

# personJSON = json.dumps(person, indent=4, sort_keys=True) # {"name": "John", "age": 30, "city": "New York", "hasChildren": false, "titles": ["engineer", "programmer"]}

# print(personJSON)

# # write json to a file
# with open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)

# # convert json to object
# person = json.loads(personJSON)
# print(person)

# # load json from a file
# with open('person.json', 'r') as file:
#     person = json.load(file)
#     print(person)

class User:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


user = User('Max', 27)


def encode_user(o):
    if isinstance(o, User):
        return {
            'name': o.name,
            'age': o.age,
            o.__class__.__name__: True
        }

from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {
            'name': o.name,
            'age': o.age,
            o.__class__.__name__: True
        }
        return JSONEncoder.default(self, 0)

userJSON = UserEncoder().encode(user)
print(userJSON)

def decode_user(d):
    if User.__name__ in d:
        return User(name=d['name'], age=d['age'])
    return d
user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user)
print(user.name)
