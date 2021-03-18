import random

import Class
import Data
data = Data.Data()

class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numOfConflicts = 0
        self._fitness = -1
        self._classNum = 0
        self._isFitnessChanged = True

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes
    def get_numOfConflicts(self): return self._numOfConflicts
    def get_fitness(self):
        if (self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):
        depts = self._data.get_depts()
        for i in range(0, len(depts)):
            courses = depts[i].get_courses()
            for j in range(0, len(courses)):
                newClass = Class.Class(self._classNum, depts[i], courses[j])
                self._classNum += 1
                newClass.set_meetingTime(data.get_meetingTimes()[random.randrange(0, len(data.get_meetingTimes()))])
                newClass.set_room(data.get_rooms()[random.randrange(0, len(data.get_rooms()))])
                newClass.set_instructor(data.get_instructors()[random.randrange(0, len(data.get_instructors()))])

                self._classes.append(newClass)
        return self

    def calculate_fitness(self):
        self._numOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            if (classes[i].get_room().get_capacity() < classes[i].get_course().get_maxNumOfStudents()):
                self._numOfConflicts += 1
            for j in range(0, len(classes)):
                if (j >= i):
                    if (classes[i].get_meetingTime() == classes[j].get_meetingTime() and classes[i].get_id() != classes[j].get_id()):
                        if (classes[i].get_room() == classes[j].get_room()): self._numOfConflicts += 1
                        if (classes[i].get_instructor() == classes[j].get_instructor()): self._numOfConflicts += 1
        return 1 / ((1.0*self._numOfConflicts + 1))

    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes) - 1):
            returnValue += str(self._classes[i]) + ", "
        returnValue += str(self._classes[len(self._classes) - 1])
        return returnValue
