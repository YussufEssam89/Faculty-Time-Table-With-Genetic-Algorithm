import prettytable as prettyTable

import Data
data = Data.Data()

class DisplayMgr:
    def print_available_data(self):
        print("> All Available Data")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_meeting_times()

    def dept_courses_data(self):
        depts = data.get_depts()
        dept_courses = []
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_courses()
            curCourses = []
            for j in range(0, len(courses)):
                curCourses.append(courses[j].get_name())
            curCourses_str = ', '.join(curCourses)
            dept_courses.insert(0, [depts[i].get_name(), curCourses_str])
        return dept_courses
    def courses_data(self):
        courses = data.get_courses()
        courses_data = []
        for i in range(0, len(courses)):
            instructors = courses.__getitem__(i).get_instructors()
            curInstructor = []
            for j in range(0, len(instructors)):
                curInstructor.append(instructors[j].get_name())
            courses_data.insert(0, [courses[i].get_number(), courses[i].get_name(), courses[i].get_maxNumOfStudents(), str(', '.join(curInstructor))])
        return courses_data
    def rooms_data(self):
        rooms = data.get_rooms()
        rooms_data = []
        for i in range(0, len(rooms)):
            rooms_data.insert(0, [rooms[i].get_number(), rooms[i].get_capacity()])
        return rooms_data
    
    def print_dept(self):
        depts = data.get_depts()
        availableDeptsTable = prettyTable.PrettyTable(['dept', 'courses'])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_courses()
            curCourses = []
            for j in range(0, len(courses)):
                curCourses.append(courses[j].get_name())
            availableDeptsTable.add_row([depts[i].get_name(), curCourses])
        print(availableDeptsTable)
    def print_course(self):
        courses = data.get_courses()
        availableDeptsTable = prettyTable.PrettyTable(['id', 'Course #', 'Max # of students', 'Instructors'])
        for i in range(0, len(courses)):
            instructors = courses.__getitem__(i).get_instructors()
            curInstructor = []
            for j in range(0, len(instructors)):
                curInstructor.append(instructors[j].get_name())
            availableDeptsTable.add_row([courses[i].get_number(), courses[i].get_name(), courses[i].get_maxNumOfStudents(), str(', '.join(curInstructor))])
        print(availableDeptsTable)
    def print_room(self):
        rooms = data.get_rooms()
        availableDeptsTable = prettyTable.PrettyTable(['Room #', 'Max Seating Capacity'])
        for i in range(0, len(rooms)):
            availableDeptsTable.add_row([rooms[i].get_number(), rooms[i].get_capacity()])
        print(availableDeptsTable)
    def print_instructor(self):
        instructors = data.get_instructors()
        availableDeptsTable = prettyTable.PrettyTable(['id', 'Instructor'])
        for i in range(0, len(instructors)):
            availableDeptsTable.add_row([instructors[i].get_id(), instructors[i].get_name()])
    def print_meeting_times(self):
        meetingTimes = data.get_meetingTimes()
        availableDeptsTable = prettyTable.PrettyTable(['id', 'Meeting Time'])
        for i in range(0, len(meetingTimes)):
            availableDeptsTable.add_row([meetingTimes[i].get_id(), meetingTimes[i].get_time()])
    def print_generation(self, population):
        generationTable = prettyTable.PrettyTable(['schedule #', 'fitness', '# of conflicts', 'classes [dept, class, room, instructor, meeting-time]'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            classes = schedules.__getitem__(i).get_classes()
            curClasses = []
            for j in range(0, len(classes)):
                curClasses.append(classes[j].get_dept().get_name() + ',' + classes[j].get_course().get_number() + ',' + classes[j].get_room().get_number() + ',' + classes[j].get_instructor().get_id() + ',' + classes[j].get_meetingTime().get_id())
            generationTable.add_row([str(i+1), round(schedules[i].get_fitness(), 3), schedules[i].get_numOfConflicts(), str(', '.join(curClasses))])
        return generationTable
    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = prettyTable.PrettyTable(['Class #', 'Dept', 'Course (number, max # of students)', 'Room (Capacity)', 'Instructor (id)', 'Meeting Time (id)'])
        for i in range(0, len(classes)):
            table.add_row([str(i+1), classes[i].get_dept().get_name(), classes[i].get_course().get_name() + ' (' + classes[i].get_course().get_number() + ', ' + str(classes[i].get_course().get_maxNumOfStudents()) + ')',  classes[i].get_room().get_number() + ' (' + str(classes[i].get_room().get_capacity()) + ')', classes[i].get_instructor().get_name() + ' (' + str(classes[i].get_instructor().get_id()) + ')', classes[i].get_meetingTime().get_time() + ' (' + str(classes[i].get_meetingTime().get_id()) + ')'])
        return table

    def get_generated(self, schedule):
        classes = schedule.get_classes()
        table_data = []
        for i in range(0, len(classes)):
            table_data.insert(0, [str(i+1), classes[i].get_dept().get_name(), classes[i].get_course().get_name() + ' (' + classes[i].get_course().get_number() + ', ' + str(classes[i].get_course().get_maxNumOfStudents()) + ')',  classes[i].get_room().get_number() + ' (' + str(classes[i].get_room().get_capacity()) + ')', classes[i].get_instructor().get_name() + ' (' + str(classes[i].get_instructor().get_id()) + ')', classes[i].get_meetingTime().get_time() + ' (' + str(classes[i].get_meetingTime().get_id()) + ')'])
        return table_data
