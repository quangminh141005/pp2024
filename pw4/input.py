# input.py
import curses
from domains.student import Student
from domains.course import Course

def inputStudent(stdscr, management):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter the number of students: ")
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
            management.students.append(Student(id, name, dob))
            row += 3
    except ValueError:
        stdscr.addstr(2, 0, "Invalid value, enter a number")

def inputCourse(stdscr, management):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter the number of courses: ")
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
                stdscr.addstr(row + 2, 0, "Enter course's credit: ")
                stdscr.refresh()
                try:
                    credit = int(stdscr.getstr().decode())
                    break
                except ValueError:
                    row += 4
                    stdscr.addstr(row, 0, "Credit must be a number! Try again.")
            management.courses.append(Course(id, name, credit))
            row += 5
    except ValueError:
        stdscr.addstr(row, 0, "Please enter a number!")
    stdscr.addstr(row + 1, 0, "Press any key to exit")
    stdscr.refresh()
    stdscr.getkey()

def inputMark(stdscr, management):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Available courses: ")
    row = 2
    for course in management.courses:
        stdscr.addstr(row, 0, f"{row - 1}. {str(course)}")
        row += 1
    stdscr.addstr(row, 0, "Enter the course ID to add mark: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode()
    if any(course_id == course.id for course in management.courses):
        for student in management.students:
            while True:
                try:
                    stdscr.addstr(row + 2, 0, f"Enter the mark for student {student.name} (ID: {student.id}): ")
                    stdscr.refresh()
                    mark = float(stdscr.getstr().decode())
                    if 0 <= mark <= 20:
                        break
                    else:
                        stdscr.addstr(row + 4, 0, "Mark must be between 0 and 20")
                except ValueError:
                    stdscr.addstr(row + 4, 0, "Invalid input")
            row += 4
            management.marks.addMark(student.id, course_id, management.roundNum(mark))
    else:
        stdscr.addstr(row + 2, 0, "Invalid course ID!")
    stdscr.addstr(row + 4, 0, "Press any key to exit")
    stdscr.refresh()
    stdscr.getkey()