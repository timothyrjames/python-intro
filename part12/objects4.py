class Pet(object):
    def __init__(self, name, age):
        # Sets the "name" property for this instance of the object.
        self.name = name
        # Sets the "age" property for this instance of the object.
        self.age = age


my_dog = Pet('Fido', 4)
print(my_dog.name)

my_cat = Pet('Tabby', 7)
print(my_cat.age)

