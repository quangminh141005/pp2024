# output.py
import curses
import numpy as np

def display_message(stdscr, message):
    stdscr.clear()
    stdscr.addstr(0, 0, message)
    stdscr.refresh()
    stdscr.getch()

def showMark(stdscr, management):
    stdscr.clear()
    stdscr.addstr(0, 0, "List of all courses: ")
    row = 2
    for course in management.courses:
        stdscr.addstr(row + 1, 0, str(course))
        row += 1
    stdscr.addstr(row + 1, 0, "Enter the course to show mark: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode().strip()
    course_mark = management.marks.getMark(course_id)
    if course_mark is not None:
        stdscr.addstr(row + 3, 0, f"Mark for course {course_id}: ")
        row += 3
        for student in management.students:
            stdscr.addstr(row + 1, 0, f"Student {student.name} (ID: {student.id}): {course_mark.get(student.id, 'Not available')}")
            row += 1
    else:
        stdscr.addstr(row + 3, 0, "Invalid course")
        row += 3
    stdscr.addstr(row + 3, 0, "Enter any key to skip: ")
    stdscr.refresh()
    stdscr.getkey()

def listStudent(stdscr, management):
    stdscr.clear()
    stdscr.addstr(0, 0, "List of all students: ")
    row = 2
    for student in management.students:
        stdscr.addstr(row, 0, str(student))
        row += 1
    stdscr.addstr(row + 1, 0, "Enter any key to skip: ")
    stdscr.refresh()
    stdscr.getkey()

def listCourse(stdscr, management):
    stdscr.clear()
    stdscr.addstr(0, 0, "List of all courses: ")
    row = 2
    for course in management.courses:
        stdscr.addstr(row + 1, 0, str(course))
        row += 1
    stdscr.addstr(row + 1, 0, "Enter any key to skip: ")
    stdscr.refresh()
    stdscr.getkey()

def sortGPA(stdscr, management):
    stdscr.clear()
    curses.echo()
    student_name = []
    GPA = []
    for student in management.students:
        student_name.append(student.name)
        GPA.append(management.showGPA(student.id))
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
    stdscr.addstr(row + 1, 0, "Enter any key to skip: ")
    stdscr.refresh()
    stdscr.getkey()

