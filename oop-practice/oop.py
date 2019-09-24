class Person(object):
    def __init__(self, person_name):
        self.name = person_name

    def say_hello(self):
        print("Hi everyone! My name is {}".format(self.name))

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def get_courses(self):
        count = len(self.courses)
        print(f"I'm taking {count} courses")
        for course in self.courses:
            print(f"   -{course}")

class Teacher(Person):
    pass

Jane = Student("Jane")
Jane.say_hello()
Jane.get_courses()

Jane.add_course("CS1.1")
Jane.add_course("BEW1.1")
Jane.add_course("SPD1.1")
Jane.get_courses()
