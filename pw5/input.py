# input.py
import curses
import zipfile
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
    with open("students.txt", "w") as student_file:
        for student in management.students:
            student_file.write(f"ID: {student.id}, Name: {student.name}, DOB: {student.dob}\n")
    
    with open("courses.txt", "w") as course_file:
        for course in management.courses:
            course_file.write(f"ID: {course.id}, Name: {course.name}, Credit: {course.credit}\n")

    with open("marks.txt", "w") as mark_file:
        for course in management.courses:
            for student in management.students:
                course_mark = management.marks.getMark(course.id)
                if course_mark is not None:
                    mark = course_mark.get(student.id,"Not available")
                else:
                    mark = "Not available"
                mark_file.write(f"Course: {course.name}, Name: {student.name}: {mark}\n")

def zip_textfile(management):
    allfiles = ["students.txt", "courses.txt", "marks.txt"]
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
        # Load students
            with open("students.txt", "r") as student_file:
                for line in student_file:
                    part = line.strip().split(", ")
                    id = part[0].split(": ")[1]
                    name = part[1].split(": ")[1]
                    dob = part[2].split(": ")[1]
                    management.students.append(Student(id, name, dob))
            
            # Load courses
            with open("courses.txt", "r") as course_file:
                for line in course_file:
                    part = line.strip().split(", ")
                    id = part[0].split(": ")[1]
                    name = part[1].split(": ")[1]
                    credit = int(part[2].split(": ")[1])

                    management.courses.append(Course(id, name, credit))
            
            # Load marks
            with open("marks.txt", "r") as mark_file:
                for line in mark_file:
                    part = line.strip().split(", ")
                    course_name = part[0].split(": ")[1]            
                    student_name = part[1].split(": ")[1]
                    mark = part[1].split(": ")[2]
                    course_id = next((c.id for c in management.courses if c.name == course_name), None)
                    student_id = next((c.id for c in management.students if c.name == student_name), None)

                    if course_id and student_id:
                        management.marks.addMark(student_id, course_id, float(mark))

            stdscr.addstr("Loading complete!\n")
        except:
            stdscr.addstr("Loading file error!\n")
    else:
        stdscr.addstr(f"{zipfile_name} not found\n") 

    

        stdscr.refresh()
        stdscr.getkey()