class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self):
        print('Here, %s!' % self.name)


my_dog = Pet('Lilly', 6)
my_dog.call()

