import math
import numpy as np
import curses

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
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"Course {self.name}, ID: {self.id}, Credit: {self.credit}"

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

    # Round to 1 decimal
    def roundNum(self, mark):
        return math.floor(mark * 10) / 10

    def inputStudent(self, stdscr):

        curses.echo()

        stdscr.clear()
        
        stdscr.addstr(0, 0, "Enter the number of  students: ")
        
        try:
            num_student = int(stdscr.getstr().decode())

            row = 2
            for _ in range(num_student):
                stdscr.addstr(row, 0, "Enter student's ID: ")
                stdscr.refresh()
                id = stdscr.getstr().decode()
                
                stdscr.addstr(row + 1, 0, "Enter student's name: ")
                stdscr.refresh()
                name = stdscr.getstr().decode()
                
                stdscr.addstr(row + 2, 0, "Enter student's DOB: ")
                stdscr.refresh()
                dob = stdscr.getstr().decode()

                self.students.append(Student(id, name, dob))

                row += 3
        except ValueError:
            stdscr.addstr(2, 0 ,"Invalid value, enter a number")

    def inputCourse(self, stdscr):

        curses.echo()

        stdscr.clear()

        stdscr.addstr(0, 0, "Enter the numbe of courses: ")
        try:
            row = 2
            num_course = int(stdscr.getstr().decode())
            
            for _ in range(num_course):

                stdscr.addstr(row, 0, "Enter course's ID: ")
                stdscr.refresh()
                id = stdscr.getstr().decode()

                stdscr.addstr(row + 1, 0, "Enter course's name: ")
                stdscr.refresh()
                name = stdscr.getstr().decode()
                
                while True:
                    stdscr.addstr(row + 2, 0 , "Enter course's credit")
                    stdscr.refresh()
                    try:
                        credit = int(stdscr.getstr().decode())
                        break
                    except ValueError:
                        row += 4
                        stdscr.addstr(row, 0, "Credit must be a number!, try agian")

                self.courses.append(Course(id, name, credit))
                row += 5
        except ValueError:
            stdscr.addstr(row, 0, "Please enter a number!")

        stdscr.addstr(row + 1, 0, "Press anykey to exit")
        stdscr.refresh()
        stdscr.getkey()

    def inputMark(self, stdscr):
        
        curses.echo()
        stdscr.clear()
        #Show the available course
        stdscr.addstr(0,0, "Avaiable course: ")

        row = 2
        for course in self.courses:
            stdscr.addstr(row, 0, f"{row - 1}. {str(course)}")
            row += 1
        
        #Check if the course is in the course list
        stdscr.addstr(row, 0, "Enter the course ID to add mark: ")
        stdscr.refresh()
        chooseCourse = stdscr.getstr().decode()

        checkCourse = any (chooseCourse ==  course.id for course in self.courses)

        #Add the mark to the course (condition: 0<=x<=20)
        if checkCourse:
            for student in self.students:
                while True:
                    try:
                        stdscr.addstr(row + 2, 0, f"Enter the mark for student {student.name} (ID: {student.id}): ")
                        stdscr.refresh()
                        mark = float(stdscr.getstr().decode())
                        if 0 <= mark <= 20:
                            break
                        else:
                            stdscr.addstr(row + 4, 0, "Mark must betweeen 0 and 20")
                    except ValueError:
                        stdscr.addstr(row + 4, 0, "Invalid input")
                row += 4
                self.marks.addMark(student.id, chooseCourse, self.roundNum(mark))

        else:
            stdscr.addstr(row + 2, 0, "Invalid course ID!!!!!")
        
        stdscr.addstr(row + 4, 0, "Press anykey to exit")
        stdscr.refresh()
        stdscr.getkey()

    def listStudent(self, stdscr):

        stdscr.clear()

        stdscr.addstr(0, 0, "List of all students: ")

        row = 2
        for student in self.students:
            stdscr.addstr(row, 0, str(student))
            row += 1

        stdscr.addstr(row + 1, 0 , "Enter any key to skip: ")
        stdscr.refresh()
        stdscr.getkey()

    def listCourse(self, stdscr):

        stdscr.clear()

        stdscr.addstr(0, 0, "List of all course: ")
        
        row = 2
        for course in self.courses:
            stdscr.addstr(row + 1, 0, str(course))
            row += 1

        stdscr.addstr(row + 1, 0, "Enter any key to skip: ")
        stdscr.refresh()
        stdscr.getkey()                     
        
    def showMark(self, stdscr):
        #List courses
        stdscr.clear()

        stdscr.addstr(0, 0, "List of all course: ")
        
        row = 2
        for course in self.courses:
            stdscr.addstr(row + 1, 0, str(course))
            row += 1
      
        # input couse
        stdscr.addstr(row + 1, 0, "Enter the course to show mark: ")
        stdscr.refresh()
        course_id = stdscr.getstr().decode().strip()

        # find course in mark
        course_mark = self.marks.getMark(course_id)
        if course_mark is not None:
            stdscr.addstr(row + 3, 0, f"Mark for course {course_id}: ")
            row += 3
            for student in self.students:
                stdscr.addstr(row + 1, 0, f"Student {student.name} (ID: {student.id}): {course_mark.get(student.id, 'Not available')}")
                row += 1
        else:
            stdscr.addstr(row + 3, 0, "Invalid course")
            row += 3
        #End
        stdscr.addstr(row + 3, 0, "Enter any key to skip: ")
        stdscr.refresh()
        stdscr.getkey() 

    def showGPA(self, student_id):
        credit_weightSum = []
        mark_weightSum = []

        for course in self.courses:
            course_marks = self.marks.getMark(course.id)
            if course_marks and student_id in course_marks:
                credit_weightSum.append(course.credit)
                mark_weightSum.append(course_marks[student_id] * course.credit)

        if credit_weightSum:
            credit_weightSum = np.array(credit_weightSum)
            mark_weightSum = np.array(mark_weightSum)

            return self.roundNum(np.sum(mark_weightSum) / np.sum(credit_weightSum))
        else:
            return 0.0     

    def sortGPA(self, stdscr):

        stdscr.clear()
        curses.echo()

        student_name = []
        GPA = []

        for student in self.students:
            student_name.append(student.name)
            GPA.append(self.showGPA(student.id))

        GPA_array = np.array(GPA)

        sorted_indices = np.argsort(GPA_array)[::-1]

        sorted_name = np.array(student_name)[sorted_indices]
        sorted_GPA = GPA_array[sorted_indices]

        stdscr.addstr(0, 0, "Student's GPA list: ")
        row = 0
        for i, (name, gpa) in enumerate(zip(sorted_name, sorted_GPA), 1):
            stdscr.addstr(row + 1, 0, f"{i}. {name}'s GPA: {gpa}")
            row += 1
        stdscr.refresh()
        #End
        stdscr.addstr(row + 1, 0, "Enter any key to skip: ")
        stdscr.refresh()
        stdscr.getkey() 

    def menu(self, stdscr):
        curses.echo()
        while True:

            stdscr.clear()

            stdscr.addstr(0, 0, "Menu: ")
            stdscr.addstr(1, 0, "1. Input student.")
            stdscr.addstr(2, 0, "2. Input course.")
            stdscr.addstr(3, 0, "3. Input mark for one course.")
            stdscr.addstr(4, 0, "4. List all the students.")
            stdscr.addstr(5, 0, "5. List all the course.")
            stdscr.addstr(6, 0, "6. Show the mark for one course. ")
            stdscr.addstr(7, 0, "7. Show sorted student's GPA:")
            stdscr.addstr(8, 0, "8. EXIT")

            stdscr.addstr(10,0, "Enter your choice:")
            stdscr.refresh()
            choose = stdscr.getstr().decode().strip()

            if choose == "1":
                self.inputStudent(stdscr)
            elif choose == "2":
                self.inputCourse(stdscr)
            elif choose == "3":
                self.inputMark(stdscr)
            elif choose == "4":
                self.listStudent(stdscr)
            elif choose == "5":
                self.listCourse(stdscr)
            elif choose == "6":
                self.showMark(stdscr)
            elif choose == "7":
                self.sortGPA(stdscr)
            elif choose == "8":
                stdscr.addstr(12, 0, "Au revoir!")
                stdscr.addstr(14, 0, "Enter any key to EXIT: ")
                stdscr.refresh()
                stdscr.getkey() 
                break
            else:
                stdscr.addstr(12, 0, "Input from 1 - 8, try again")
                stdscr.addstr(14, 0, "Enter any key to EXIT: ")
                stdscr.refresh()
                stdscr.getkey() 

if __name__ == "__main__":
    mana = Management()
    curses.wrapper(mana.menu)

    