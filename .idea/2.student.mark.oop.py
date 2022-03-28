def getStudentNum ():
    return int (input ("Enter number of students: "))

def getCourseNum ():
    return int (input ("Enter number of courses: "))

def getCourseDetails ():
    courseid = input ("Enter course id: ")
    coursename = input ("Enter course name: ")
    return courseid, coursename

def getStudentDetails ():
    studentid = input ("Enter student id: ")
    studentname = input ("Enter student name: ")
    studentdob = input ("Enter student's date of birth: ")
    return studentid, studentname, studentdob

def getMarks (studentid, courseid):
    prompt = f"Enter marks for student {studentid} for course {courseid}: ".format (studentid, courseid)
    input (prompt)

nStudents = getStudentNum ()
studentList = []
for i in range (nStudents):
    studentid, nm, dob = getStudentDetails ()
    studentLst.append ((studentid, nm, dob))

nCourses = getCourseNum ()
courseList = []
for i in range (nCourses):
    courseid, coursename = getCourseDetails ()
    courseList.append ((courseid, coursename))

d = {}
n = int (input ("Enter how many student-course marks do you want to enter? "))
for i in range (n):
    while True:
        studentid = input ("Enter student id: ")
        courseid = input ("Enter course id: ")
        if studentid not in [student [0] for student in studentLst]:
            print ("Bad student id")
            continue
        if courseid not in [course [0] for course in courseLst]:
            print ("Bad course id")
            continue
        break
    marks = int (input ("Enter marks: "))
    if courseid in d:
        d [courseid].append ((studentid, marks))
        print(type(d [courseid]))#list
    else:
        d [courseid] = [(studentid, marks)]
        print(type(courseid))#cid is string

print ("\nListing all students now..")
for s in studentList:
    print (f"Student id: {s[0]} Name: {s[1]} Date of birth: {s[2]}")

print ("\nListing all courses now..")
for c in courseList:
    print (f"Course id: {c[0]} Name: {c[1]}")

courseid = input ("\nWhich course do you want to see all student marks for? ")
if courseid in d:
    for tups in d [courseid]:
        print (f"Student {tups[0]} got {tups [1]} marks")