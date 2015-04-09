import sys
import copy

class ClassReg:

    def __init__(self):
        self.class_dict={}
        self.student_dict={}

    def addClass(self, id, capacity, time):
        self.class_dict[id] = {"capacity":capacity, "time":time, "student":[]}

    def removeClass(self, id):
        student_list = copy.copy(self.class_dict[id]["student"])
        for student_id in student_list:
            self.unenrollStudent(student_id, id)

        if len(self.class_dict[id]["student"])!=0:
            print "ERROR: not 0 when removeClass"
            #print self.class_dict[id]["student"]
            exit(0)
        del self.class_dict[id]

    def infoClass(self, id):
        print "class id " + str(id)
        print self.class_dict[id]["student"]


    def addStudent(self, id, capacity, start, end):
        self.student_dict[id] = {"capacity":capacity, "start":start, "end":end, "class":[]}

    def removeStudent(self, id):
        # remove student from student's classes
        class_list = copy.copy(self.student_dict[id]["class"])
        for class_id in class_list:
            self.unenrollStudent(id, class_id)

        # remove he
        if len(self.student_dict[id]["class"])!=0:
            print "ERROR: class not 0 when removestudents"
            #print self.student_dict[id]["class"]
            exit(0)
        del self.student_dict[id]


    def infoStudent(self, id):
        print "student id:" + str(id)
        print self.student_dict[id]["class"]

    def enrollStudent(self, studentId, classId):
        # need to check time, check capa
        self.student_dict[studentId]["class"].append(classId)
        self.class_dict[classId]["student"].append(studentId)

    def unenrollStudent(self, studentId, classId):

        if classId in self.student_dict[studentId]["class"]:
            self.student_dict[studentId]["class"].remove(classId)
        if studentId in self.class_dict[classId]["student"]:
            self.class_dict[classId]["student"].remove(studentId)
            #print "remove sutdentID %d from classId %d" % (studentId, classId)


if __name__ == "__main__":


    classSys=ClassReg()
    classSys.addClass(0, 100, 2015)
    classSys.addClass(1, 200, 2015)
    classSys.addClass(2, 200, 2015)
    classSys.addClass(3, 200, 2015)

    classSys.addStudent(0, 1, 3, 0)
    classSys.addStudent(1, 1, 3, 0)


    classSys.enrollStudent(0, 1)
    classSys.enrollStudent(1, 0)
    classSys.enrollStudent(1, 1)
    classSys.enrollStudent(1, 2)


    print classSys.class_dict
    print classSys.student_dict

    classSys.removeStudent(1)

    print "--------"
    print classSys.class_dict
    print classSys.student_dict

