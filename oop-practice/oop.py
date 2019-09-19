class Person(object):
    def __init__(self, person_name, hair_color):
        self.name = person_name
        self.hairColor = hair_color
    def say_hello(self):
        print("Hi everyone! My name is {}".format(self.name))
        print("My hair color is {}".format(self.hairColor))

John = Person("Gonzo","Black")


John.say_hello()
