def getCourseNumber():
    return int(input("Enter the number of courses: "))


def getStudentNumber():
    return int(input("Enter the number of students: "))


def getCourseInfo(n):
    idcourse = input(f"Enter course{n}'s ID: ")
    namecourse = input(f"Enter course{n}'s name: ")
    return idcourse, namecourse


def getStudentInfo(i):
    namestudent = input(f"Enter student{i}'s name: ")
    dobstudent = input(f"Enter student{i}'s DOB: ")
    idstudent = input(f"Enter student{i}'s ID: ")
    return namestudent, dobstudent, idstudent


def enterMarks(studentid, courseid):
    return int(input("Enter mark of student" + studentid + "for course" + courseid))


def ListStudents(studentLst):
    print("Printing all students infos: ")
    for i in studentLst:
        print(f"Student id: {i[2]}, Name: {i[0]}, DOB: {i[1]}")


def ListCourses(courseLst):
    print("Printing all courses infos: ")
    for j in courseLst:
        print(f"Course id: {j[0]}, Name: {j[1]}")


def getStudentList(n):
    StudentLst = []
    for i in range(n):
        namestudent, dobstudent, idstudent = getStudentInfo(i+1)
        StudentLst.append((namestudent, dobstudent, idstudent))
    return StudentLst


def getCourseList(n):
    CourseLst = []
    for i in range(n):
        idcourse, namecourse = getCourseInfo(i+1)
        CourseLst.append((idcourse, namecourse))
    return CourseLst


def listMarks(markLst):
    idcourse = input("\n Get students marks for which course? ")
    for student in markLst[idcourse]:
        print("Student" + student[0] + " got " + student[1] + "marks")


def enterMarks(markLst):
    n = int(input("Number of students to fill: "))
    for i in range(n):
        idstudent = input("Student Id ? ")
        idcourse = input("Course Id: ")
        mark = int(input("Marks"))
        if idcourse in markLst:
            markLst[idcourse].append((idstudent, mark))
        else:
            markLst[idcourse] = [(idstudent, mark)]
    return markLst


def main():
    StudentsNum = getStudentNumber()
    studentLst = getStudentList(StudentsNum)
    CourseNum = getCourseNumber()
    courseLst = getCourseList(CourseNum)
    markLst = {}

    while True:
        print(" 1: To fill students marks")
        print(" 2: To show students list")
        print(" 3: To show course list")
        print(" 4: To show mark for course")
        print(" 5: To exit")

        k = int(input("Choose desired option: "))
        if k == 1:
            enterMarks(markLst)
        elif k == 2:
            ListStudents(studentLst)
        elif k == 3:
            ListCourses(courseLst)
        elif k == 4:
            listMarks(markLst)
        elif k == 5:
            break
        else:
            print("Invalid choice")
        return


if __name__ == "__main__":
    main()
