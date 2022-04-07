class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self):
        print(self.get_call())

    def get_call(self):
        return 'Here, %s!' % self.name

    def __str__(self):
       return self.name + ' is ' + str(self.age)


my_cat = Pet('Heathcliff', 4)
print(my_cat)

