def inputStudent():
    numb = int(input("Enter the number of student: "))
    return numb

def inputStudentInfo(numb):
    students = []
    for i in range(numb):
        id = input("Type the student's id: ").strip()
        name = input("Enter the student name: ").strip()
        dob = input("Enter the student date of bith: ").strip()
        student = {"id": id, "name": name, "dob": dob}

        students.append(student)
    return students

def inputCourse():
    numb = int(input("Enter the number of courses: "))
    return numb

def inputCourseInfo(num):
    courses = []
    for i in range(num):
        id = input("Enter the course id: ")
        name = input("Enter the course name: ")
        course = {"id": id, "name": name}
        courses.append(course)

    return courses    

def inputMark(students, courses):
    print("Available courses: ")
    for i, course in enumerate(courses, start = 1):
        print(f"{i}.{course['name']}(ID:{course['id']})")
    courseID = input("Enter the ID of the course to input mark: ")
    
    if any(courseID == course['id'] for course in courses):
        #code
        if courseID not in marks:
            marks[courseID] = {}
        
        for student in students:
            while True:
                try: 
                    mark = float(input(f"Enter the mark for student {student['name']} (ID: {student['id']})"))
                    if 0 <=mark<= 20:
                        break
                    else:
                        print("Enter the mark between 0 and 20.")
                except ValueError:
                    print("INVALID INPUT")

            marks[courseID][student['id']] = mark

    else:
        print("Invalid Course ID!")
        exit()

    return marks

def listCourses(courses):
    print("\nListing all the courses: ")
    for course in courses:
        print(f"Course: {course['id']}, course name: {course['name']}:")


def listStudent(students):
    print("\nListing all the students: ")
    for student in students:
        print(f"{student}")

def listStudentMark(marks, courses, students):
    listCourses(courses)
    
    courseID = input("Enter the course to view mark: ")

    if courseID in marks:
        print(f"Mark for course {courseID}: ")
        for student in students:
            mark = marks[courseID].get(student['id'], "No mark available")
            print(f"Student {student['name']} (ID: {student['id']}: {mark})")
    else: print("Invalid course ID")


num_students = inputStudent()
students = inputStudentInfo(num_students)

num_courses = inputCourse()
courses = inputCourseInfo(num_courses)

marks = {}

while True:
    print("\nMenu:")
    print("1. Input marks for a course")
    print("2. List all students")
    print("3. List all the courses")
    print("4. List student marks for a course")
    print("5. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        inputMark(students, courses)
    elif choice == "2":
        listStudent(students)
    elif choice == "3":
        listCourses(courses)
    elif choice == "4":
        listStudentMark(marks, courses, students)
    elif(choice == "5"):
        print("Goodbyeeee")
        break
    else: print("Invalid, try agian")







