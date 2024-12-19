class Person:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Dob: {self.dob}"

class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Course {self.name}, ID: {self.id}"

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

class Management:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()

    def inputStudent(self):
        num_student = int(input("Enter the number of sudents: "))
        for _ in range(num_student):
            id = input("Enter the student ID: ")
            name = input("Enter the student name: ")
            dob = input("Enter the sudent date of birth: ")
            self.students.append(Student(id, name, dob))

    def inputCourse(self):
        num_course = int(input("Enter the numbe of courses: "))
        for _ in range(num_course):
            id = input("Enter the ID for the course: ")
            name = input("Enter the course name: ")
            self.courses.append(Course(id, name))

    def inputMark(self):
        #Show the available course
        print("\nAvailable course: ")
        for course in self.courses:
            print(course)
        
        #Check if the course is in the course list
        chooseCourse = input("Enter the course ID to add mark: ")
        checkCourse = any (chooseCourse ==  course.id for course in self.courses)

        #Add the mark to the course (condition: 0<=x<=20)
        if checkCourse:
            for student in self.students:
                while True:
                    try:
                        mark = int(input(f"Enter the mark for student {student.name} (ID: {student.id}): "))
                        if 0 <= mark <= 20:
                            break
                        else:
                            print("Mark must betweeen 0 and 20")
                    except ValueError:
                        print("Invalid input")
                self.marks.addMark(student.id, chooseCourse, mark)
        else:
            print("Invalid course ID!!!!!")

    def listStudent(self):
        print("\nList of all students: ")
        for student in self.students:
            print(student)

    def listCourse(self):
        print("\nList of all course: ")
        for course in self.courses:
            print(course)

    def showMark(self):
        self.listCourse()
        # input couse
        course_id = input("Enter the course to show mark: ").strip()

        # find course in mark
        course_mark = self.marks.getMark(course_id)
        if course_mark is not None:
            print(f"\nMark for course {course_id}")
            for student in self.students:
                print(f"Student {student.name} (ID: {student.id}): {course_mark.get(student.id, 'Not available')}")
        else:
            print("Invalid course")

    def menu(self):
        while True:
            print("\nMenu: ")
            print("1. Input student.")
            print("2. Input course.")
            print("3. Input mark for one course.")
            print("4. List all the students.")
            print("5. List all the course.")
            print("6. Show the mark for one course.")
            print("7. Exit")

            choose = input("Enter your choice: ")

            if choose == "1":
                self.inputStudent()
            elif choose == "2":
                self.inputCourse()
            elif choose == "3":
                self.inputMark()
            elif choose == "4":
                self.listStudent()
            elif choose == "5":
                self.listCourse()
            elif choose == "6":
                self.showMark()
            elif choose == "7":
                print("Au revoir!")
                break
            else:
                print("Input from 1 - 7, try again!")

if __name__ == "__main__":
    mana = Management()
    mana.menu()