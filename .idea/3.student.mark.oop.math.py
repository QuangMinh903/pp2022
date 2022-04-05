import math
import numpy as np
class Stu:

    def input(self):
        self.sid = input(f"Enter id: ")
        self.sname = input("Enter name: ")
        self.studentdob = input("Enter date of birth: ")
        self.gpa = 0

    def print(self):
        print("Student's id: {}".format(self.sid))
        print("Student's name: {}".format(self.sname))
        print("Student's date of birth: {}".format(self.studentdob))


class Cour:
    def __init__(self):
        self.mark = []

    def input(self):
        print("Type course's information")
        self.cid = input(f"Enter course's id: ")
        self.sname = input("Enter student's name: ")

    def print(self):
        print("Course's id: {}".format(self.cid))
        print("Course's name: {}".format(self.sname))

    def addMa(self, stu, mark):
        self.mark.append({
            'stu': stu,
            'ma': mark
        })

    def printMa(self):
        tmp = {}
        for mark in self.mark:
            if mark['stu'] not in tmp.keys():
                tmp[mark['stu']] = [str(mark['ma'])]
            else:
                tmp[mark['stu']].append(str(mark['ma']))
        for key, value in tmp.items():
            print("Student {} have {} mark is: {}".format(
                key, len(value), ", ".join(value)))

class Class:
    def __init__(self):
        self.stuList = []
        self.courList = []

    def inputCour(self):
        n = int(input("Enter the number of courses: "))
        for i in range(n):
            cour = Cour()
            cour.input(i+1)
            self.courList.append(cour)


    def inputStu(self):
        n = int(input("Enter the number of students: "))
        for i in range(n):
            stu = Stu()
            stu.input(i+1)
            self.stuList.append(stu)

    def Stunumb(self):
        return len(self.stuList)

    def Cournumb(self):
        return len(self.courList)

    def inputMa(self):
        courIdx = None
        while True:
            courId = input("Enter course id: ")
            courIdx = self.__checkCour(courId)
            if courIdx is None:
                print("Course does not exist")
            else:
                break
        n = int(input("Enter how many student do you want to fill marks? "))
        for i in range(n):
            studentId = ""
            while True:
                studentId = input("Enter student id {}: ".format(i+1))
                if not self.__checkValidStudent(studentId):
                    print("Student does not exist")
                else:
                    break
            mark = int(input("Enter marks: "))
            courseIdx.addMark(studentId, mark)

    def listStu(self):
        print("Class have {} students".format(self.Stunumb()))
        for stu in self.stuList:
            stu.print()
            print("")

    def listCour(self):
        print("Class have {} courses".format(self.Cournumb()))
        for cour in self.courList:
            cour.print()
            print("")

    def showMarkByCourse(self):
        while True:
            courId = input("Enter course id: ")
            cour = self.__checkCour(courId)
            if courId is None:
                print("Course does not exist")
            else:
                cour.printMa()

    def __checkCour(self, courId):
        for cour in self.courList:
            if courId == cour.id:
                return cour
        return None

    def __checkStudent(self, stuId):
        for stu in self.stuList:
            if stuId == stu.id:
                return True
        return False

    _class = Class()
    _class.inputStu()
    _class.inputCour()
    while True:
        print("Choose 1: To fill student's mark with student ID and course ID")
        print("Choose 2: To list all students")
        print("Choose 3: To list all courses")
        print("Choose 4: To list all mark in a course")
        print("Choose 5: To exit")

        n = int(input("Please choose? "))
        if n == 1:
            _class.inputMa()
        elif n == 2:
            _class.listStu()
        elif n == 3:
            _class.listCour()
        elif n == 4:
            _class.printMa()
        elif n == 5:
            break
        else:
            print("PLease choose again from 1-5")
    return


if __name__ == '__main__':
    main()