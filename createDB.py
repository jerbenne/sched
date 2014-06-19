#!/usr/bin/python

import sqlite3 as lite
import sys
import codecs

class DbCreator():

    inClass = False

    def createDB(self, tup):

        con = lite.connect('courses.db')

        with con:
            cur = con.cursor()

            cur.execute("DROP TABLE IF EXISTS Courses")
            cur.execute("""CREATE TABLE Courses(SubjectCode TEXT, ClassNo INT,
                ClassName TEXT, ClassDay TEXT, ClassTime TEXT, Professor TEXT,
                CRN INT, EnrollStatus TEXT, OpenSpots INT)""")
            cur.executemany("INSERT INTO Courses VALUES(?,?,?,?,?,?,?,?,?)", tup)


def main(argv):

    sys.stdout = codecs.getwriter('utf8')(sys.stdout)

    tup = [('CS', '161', 'Introduction to Computing', 'R', '06:30 pm - 09:20 pm', 'Olga V Kerchentseva', '40152', 'FULL', 0), ('CS', '172', 'Computer Programming II', 'W', '06:00 pm - 08:50 pm', 'David Harris Augenblick', '40416', 'FULL', 0), ('CS', '172', 'Computer Programming II', 'R', '06:00 pm - 08:50 pm', 'David Harris Augenblick', '43133', 'Max enroll=30; Enroll=28', 2), ('CS', '260', 'Data Structures', 'MWF', '10:00 am - 10:50 am', 'Krzysztof  Nowak', '40084', 'FULL', 0), ('CS', '260', 'Data Structures', 'M', '06:00 pm - 08:50 pm', 'Krzysztof  Nowak', '40487', 'FULL', 0), ('CS', '260', 'Data Structures', 'T', '06:00 pm - 08:50 pm', 'Timothy W Cheeseman', '43287', 'FULL', 0), ('CS', '275', 'Web and Mobile App Development', 'TR', '09:30 am - 10:50 am', 'William Marc Mongan', '42201', 'Max enroll=25; Enroll=14', 11), ('CS', '275', 'Web and Mobile App Development', 'TR', '11:00 am - 12:20 pm', 'David Harris Augenblick', '42202', 'Max enroll=25; Enroll=24', 1), ('CS', '275', 'Web and Mobile App Development', 'TR', '12:30 pm - 01:50 pm', 'David Harris Augenblick', '42203', 'Max enroll=25; Enroll=13', 12), ('CS', '283', 'Systems Programming', 'M', '03:00 pm - 03:50 pm', '02:00 pm - 03:50 pm', '42097', 'Max enroll=35; Enroll=31', 4), ('CS', '283', 'Systems Programming', 'M', '06:00 pm - 08:50 pm', 'Louis A Kratz', '42166', 'FULL', 0), ('CS', '283', 'Systems Programming', 'MWF', '01:00 pm - 01:50 pm', 'Nagarajan  Kandasamy', '43367', 'Max enroll=10; Enroll=1', 9), ('CS', '338', 'Graphical User Interfaces', 'W', '06:00 pm - 08:50 pm', 'Maxim D Peysakhov', '40631', 'Max enroll=30; Enroll=25', 5), ('CS', '345', 'Computer Game Design ', 'M', '11:00 am - 01:50 pm', 'STAFF', '41113', 'Max enroll=7; Enroll=6', 1), ('CS', '360', 'Programming Language Concepts', 'R', '06:30 pm - 09:20 pm', 'Krzysztof  Nowak', '40632', 'Max enroll=30; Enroll=22', 8), ('CS', '360', 'Programming Language Concepts', 'TR', '02:00 pm - 03:20 pm', 'Krzysztof  Nowak', '42168', 'FULL', 0), ('CS', '365', 'System Administration', 'TR', '12:30 pm - 01:50 pm', 'Gaylord Campbell Holder', '40844', 'Max enroll=25; Enroll=8', 17), ('CS', '370', 'Operating Systems', 'TR', '03:30 pm - 04:50 pm', 'William Marc Mongan', '40140', 'Max enroll=30; Enroll=13', 17), ('CS', '451', 'Software Engineering', 'T', '06:30 pm - 09:20 pm', 'Sunny  Wong', '40825', 'FULL', 0), ('CS', '480', 'ST:Autonomous Agents', 'T', '06:30 pm - 09:20 pm', 'Robert Nelson Lass', '42707', 'FULL', 0), ('CS', '500', 'Database Theory', 'M', '06:00 pm - 08:50 pm', 'Julia  Stoyanovich', '42710', 'Max enroll=25; Enroll=11', 14), ('CS', '500', 'Database Theory', 'TBD', 'TBD', 'Julia  Stoyanovich', '42711', 'FULL', 0), ('CS', '680', 'ST:Autonomous Agents', 'T', '06:30 pm - 09:20 pm', 'Robert Nelson Lass', '42708', 'Max enroll=15; Enroll=3', 12), ('CS', '680', 'ST:Autonomous Agents', 'TBD', 'TBD', 'Robert Nelson Lass', '42709', 'Max enroll=20; Enroll=19', 1), ('CS', '997', 'Research in Computer Science', 'TBD', 'TBD', 'Ali  Shokoufandeh', '43385', 'FULL', 0)]

    dbCreator = DbCreator()
    dbCreator.createDB(tup)
    
if __name__ == "__main__":
    main(sys.argv[1:])
