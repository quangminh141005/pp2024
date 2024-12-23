class Person:

    def __init__(self, id, name, dob):

        self.id = id

        self.name = name

        self.dob = dob



    def __str__(self):

        return f"ID: {self.id}, Name: {self.name}, Dob: {self.dob}"
