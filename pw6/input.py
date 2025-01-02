# input.py
import curses
import zipfile
import pickle
import os
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
    stdscr.addstr(row + 1, 0, "Press any key to exit")
    stdscr.refresh()
    stdscr.getkey()

def savefile(management):
    # Serialize to binary file
    with open("student.pickle", "wb") as  student_file:
        pickle.dump(management.students, student_file)

    with open("course.pickle", "wb") as course_file:
        pickle.dump(management.courses, course_file)

    with open("mark.pickle", "wb") as mark_file:
        pickle.dump(management.marks, mark_file)

def zip_textfile(management):
    allfiles = ["student.pickle", "course.pickle", "mark.pickle"]
    zipfile_name = "students.dat"

    with zipfile.ZipFile(zipfile_name, "w") as zipf:
        for file in allfiles:
            zipf.write(file)

def checkfile(stdscr, management):

    stdscr.clear()

    # Check if file exist
    zipfile_name = "students.dat"
    if os.path.exists(zipfile_name):
        stdscr.addstr(f"{zipfile_name} founded, Loading...\n")
        stdscr.refresh()
        with zipfile.ZipFile(zipfile_name, "r") as zipf:
            zipf.extractall()

        try:
            with open("student.pickle", "rb") as student_file:
                management.students = pickle.load(student_file)

            with open("course.pickle", "rb") as course_file:
                management.courses = pickle.load(course_file)

            with open("mark.pickle", "rb") as mark_file:
                management.marks = pickle.load(mark_file)

            stdscr.addstr("Loading complete!\n")
        except:
            stdscr.addstr("Loading file error!\n")
    else:
        stdscr.addstr(f"{zipfile_name} not found\n") 

    

        stdscr.refresh()
        stdscr.getkey()