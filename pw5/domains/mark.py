class Mark:
    def __init__(self):
        self.marks = {}

    def addMark(self, student_id, course_id, mark):
        if course_id not in self.marks:
            self.marks[course_id] = {}
        self.marks[course_id][student_id] = mark

    def getMark(self, course_id):
        if course_id in self.marks:
            return self.marks[course_id]
        return None