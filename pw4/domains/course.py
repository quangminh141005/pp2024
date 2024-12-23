class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"Course {self.name}, ID: {self.id}, Credit: {self.credit}"