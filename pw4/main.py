# main.py
import curses
from input import inputStudent, inputCourse, inputMark
from output import showMark, listStudent, listCourse, sortGPA
from domains.mark import Mark
from domains.student import Student
from domains.course import Course

class Management:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()

    def roundNum(self, mark):
        return round(mark, 1)

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

    def menu(self, stdscr):
        curses.echo()
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Menu: ")
            stdscr.addstr(1, 0, "1. Input student.")
            stdscr.addstr(2, 0, "2. Input course.")
            stdscr.addstr(3, 0, "3. Input mark for one course.")
            stdscr.addstr(4, 0, "4. Show the mark for one course.")
            stdscr.addstr(5, 0, "5. List all the students.")
            stdscr.addstr(6, 0, "6. List all the courses.")
            stdscr.addstr(7, 0, "7. Show sorted student's GPA.")
            stdscr.addstr(8, 0, "8. EXIT")
            stdscr.addstr(10, 0, "Enter your choice: ")
            stdscr.refresh()
            choose = stdscr.getstr().decode().strip()
            if choose == "1":
                inputStudent(stdscr, self)
            elif choose == "2":
                inputCourse(stdscr, self)
            elif choose == "3":
                inputMark(stdscr, self)
            elif choose == "4":
                showMark(stdscr, self)
            elif choose == "5":
                listStudent(stdscr, self)
            elif choose == "6":
                listCourse(stdscr, self)
            elif choose == "7":
                sortGPA(stdscr, self)
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