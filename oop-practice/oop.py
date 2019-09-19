class Person(object):
    def __init__(self, person_name, hair_color, age):
        self.name = person_name
        self.hairColor = hair_color
        self.age = age
    def say_hello(self):
        print("Hi everyone! My name is {}".format(self.name))
        print("My hair color is {}".format(self.hairColor))
        print("My age is {}".format(self.age))

John = Person("Gonzo","Black","18")


John.say_hello()
