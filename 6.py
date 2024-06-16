from collections import namedtuple
jane_dict = {"name": "Jane", "age": 25, "height": 1.75}
jane_dict["age"] = 26
jane_dict["weight"] = 67
print(jane_dict)
Person = namedtuple("Person", "name age height")
jane = Person(**jane_dict)
print(jane)
jane = jane._replace(age=26, weight=67)
print(jane)
