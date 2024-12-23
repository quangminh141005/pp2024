from .person.py import Person

class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)