class Person:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DOB: {self.dob}"


class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Course ID: {self.id}, Name: {self.name}"

class Mark:
    def __init__(self):
        self.marks = {}

    def addMark(self, course_id, student_id, mark):
        if course_id not in self.marks:
            self.marks[course_id] = {}
        self.marks[course_id][student_id] = mark

    def getMark(self, courseID):
        if courseID in self.marks:
            return {student.id: self.marks[courseID].get(student.id, "Not available")}
        return None

class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()
    
    def inputStudent(self):
        numStudents = int(input("Enter the number of student: "))
        for i in range (numStudents):
            id = input("Enter the student ID:").strip()
            name = input("Enter the student name: ").strip()
            dob = input("Enter the student date of birth: ").strip()
            self.students.append(Student(id, name, dob))

    def inputCourse(self):
        numCourses = int(input("Enter the number of course: "))
        for i in range(numCourses):
            id = input("Enter the number of course ID: ")
            name = input("Enter the number of course name:") 
            self.courses.append(Course(id, name))

    def inputMark(self):
        print("\nAvailable Course: ")
        for course in self.courses:
            print(course)

        courseID = input("Enter the id of the course to input mark: ").strip()
        courseFound = any(course.id == courseID for course in self.courses)

        if courseFound:
            for student in self.students:
                while True:
                    try:
                        mark = float(input(f"Enter the mark for student {student.name} (ID: {student.id}: )"))
                        if 0 <= mark <= 20:
                            break
                        else:
                            print("Mark must be between 0 and 20")
                    except ValueError:
                        print("Invalid input")
                self.marks.addMark(courseID, student.id, mark)
        else:
            print("Invalid cousre ID!")

    def listStudents(self):
        print("\nList of students:")
        for student in self.students:
            print(student)

    def listCourses(self):
        print("\nList of courses: ")
        for course in self.courses:
            print(course)

    def listStudentMark(self):
        self.listCourses()
        course_id = input("Enter the course id to view mark: ").strip()
        marks = self.marks.getMark(course_id)

        if marks is not None:
            print(f"\nMark for course {course_id}: ")
            for student in  self.students:
                print(f"{student.name} (ID: {student.id}): {marks.get(student.id, "Not available")}")
        else:
            print("Invalid course ID")
    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks")
            print("4. List students")
            print("5. List courses")
            print("6. List student marks")
            print("7. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.inputStudent()
            elif choice == "2":
                self.inputCourse()
            elif choice == "3":
                self.inputMark()
            elif choice == "4":
                self.listStudents()
            elif choice == "5":
                self.listCourses()
            elif choice == "6":
                self.listStudentMark()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
    
if __name__ == "__main__":
    ms = ManagementSystem()
    ms.menu()