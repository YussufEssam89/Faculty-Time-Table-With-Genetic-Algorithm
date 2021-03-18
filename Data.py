import sqlite3 as sqlite
import os.path

import Room
import MeetingTime
import Instructor
import Course
import Department

class Data:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "faculty_timetable_db.db")
        self._conn = sqlite.connect(db_path)
        self._c = self._conn.cursor()
        self._rooms = self.select_rooms()
        self._meetingTimes = self.select_meeting_times()
        self._instructors = self.select_instructors()
        self._courses = self.select_courses()
        self._depts = self.select_depts()
        self._numberOfClasses = 0
        for i in range(0, len(self._depts)):
            self._numberOfClasses += len(self._depts[i].get_courses())

    def select_rooms(self):
        self._c.execute("SELECT * FROM room")
        rooms = self._c.fetchall()
        returnRooms = []
        for i in range(0, len(rooms)):
            returnRooms.append(Room.Room(rooms[i][0], rooms[i][1]))
        return returnRooms

    def select_meeting_times(self):
        self._c.execute("SELECT * FROM meeting_time")
        meetingTimes = self._c.fetchall()
        returnMeetingTimes = []
        for i in range(0, len(meetingTimes)):
            returnMeetingTimes.append(MeetingTime.MeetingTime(meetingTimes[i][0], meetingTimes[i][1]))
        return returnMeetingTimes

    def select_instructors(self):
        self._c.execute("SELECT * FROM instructor")
        instructors = self._c.fetchall()
        returnInstructors = []
        for i in range(0, len(instructors)):
            returnInstructors.append(Instructor.Instructor(instructors[i][0], instructors[i][1]))
        return returnInstructors

    def select_courses(self):
        self._c.execute("SELECT * FROM courses")
        courses = self._c.fetchall()
        returnCourses = []
        for i in range(0, len(courses)):
            returnCourses.append(Course.Course(courses[i][0], courses[i][1], self.select_course_instructors(courses[i][0]), courses[i][2]))
        return returnCourses

    def select_depts(self):
        self._c.execute("SELECT * FROM departments")
        depts = self._c.fetchall()
        returnDepts = []
        for i in range(0, len(depts)):
            returnDepts.append(Department.Department(depts[i][0], self.select_dept_courses(depts[i][0])))
        return returnDepts

    def select_course_instructors(self, courseNumber):
        self._c.execute("SELECT * FROM course_instructor where course_number == '" + courseNumber + "'")
        dbInstructorNumbers = self._c.fetchall()
        instructorNumbers = []
        for i in range(0, len(dbInstructorNumbers)):
            instructorNumbers.append(dbInstructorNumbers[i][1])
        returnValue = []
        for i in range(0, len(self._instructors)):
            if self._instructors[i].get_id() in instructorNumbers:
                returnValue.append(self._instructors[i])
        return returnValue

    def select_dept_courses(self, deptName):
        self._c.execute("SELECT * FROM dept_course where dept_name == '" + deptName + "'")
        dbCourseNumbers = self._c.fetchall()
        courseNumbers = []
        for i in range(0, len(dbCourseNumbers)):
            courseNumbers.append(dbCourseNumbers[i][1])
        returnValue = []
        for i in range(0, len(self._courses)):
            if self._courses[i].get_number() in courseNumbers:
                returnValue.append(self._courses[i])
        return returnValue

    def get_rooms(self): return self._rooms
    def get_instructors(self): return self._instructors
    def get_courses(self): return self._courses
    def get_depts(self): return self._depts
    def get_meetingTimes(self): return self._meetingTimes
    def get_numberOfClasses(self): return self._numberOfClasses
