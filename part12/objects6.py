class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self):
        print(self.get_call())

    def get_call(self):
        return 'Here, %s!' % self.name


my_dog = Pet('Lilly', 6)
call = my_dog.get_call()
print(call)
print(call)

