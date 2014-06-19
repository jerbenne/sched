from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib2
import sys
import string
import codecs




class MyHTMLParser(HTMLParser):

    inClass = False
    foundSubjectCode = False

    professor = ""
    CRN = 0
    classTime = ""
    classDay = ""
    className = ""
    classNumber = 0
    subjectCode = "not a subject code"
    openSpots = 0
    enrollStatus = ""

    dataPos = 0
    classTuples = []


    def printClass(self):
        print 'Professor:',self.professor
        print 'CRN:',self.CRN
        print 'Class Time:',self.classTime
        print 'Class Day:',self.classDay
        print 'Class Name:',self.className
        print 'Class Number:', self.classNumber
        print 'Subject Code:', self.subjectCode 
        print '\n'

    def addClass(self):
        tup = (self.subjectCode, self.classNumber, self.className, self.classDay, self.classTime,
                self.professor, self.CRN, self.enrollStatus, self.openSpots) 
				
        self.classTuples.append(tup)

    def handle_starttag(self, tag, attrs):
        #print "Start tag:",tag
        #for attr in attrs:
        #    print "     attr:", attr


        #attrs will be in format: [('title', 'FULL')] or
        # [('title', 'Max enroll=30; Enroll=28')
        if tag == 'p' and attrs:
            if attrs[0][0] == 'title':
                enrollTuple = attrs[0]
                enrollCount = enrollTuple[1]

                #Max enroll=30; Enroll=28
                #semicolon implies there's a max and current enroll
                pos1 = string.find(enrollCount, ';')
                if pos1 != -1: 
                    self.enrollStatus = enrollCount
                    pos2 = string.find(enrollCount, '=')
                    pos3 = string.rfind(enrollCount, '=')

                    maxEnroll = enrollCount[pos2+1:pos1]
                    currEnroll = enrollCount[pos3+1:]

                    self.openSpots = int(maxEnroll) - int(currEnroll)

                else:
                    self.enrollStatus = 'FULL';
                    self.openSpots = 0
                
                print 'Enroll status:', self.enrollStatus
                print 'Spots open:', self.openSpots
			

    def handle_endtag(self, tag):
        x = 5
        #print "End tag  :", tag
    def handle_data(self, data):

        if not self.foundSubjectCode:
            if string.find(data, 'Subject Code') != -1:
                self.foundSubjectCode = True
                s = string.split(data, 'Subject Code ')
                self.subjectCode = s[1]
  

        if data == self.subjectCode:
            self.inClass = True
            self.dataPos = 0
 
        if self.inClass:

            if self.dataPos == 2:
                self.classNumber = data
            elif self.dataPos == 11:
                self.CRN = data
            elif self.dataPos == 13:
                self.className = data
            elif self.dataPos == 18:
                if data.strip():  
                    self.classDay = data
                else:
                    self.dataPos -= 1 #extra blank data filed when professor is TBD
            elif self.dataPos == 20:
                self.classTime = data
            elif self.dataPos == 25:
                self.professor = data
                self.inClass = False
                self.printClass()
                self.addClass()
           
            self.dataPos += 1
            
    def handle_comment(self, data):
        x = 5
        #print "Comment  :", data
    def handle_entityref(self, name):
        x = 5
        c = unichr(name2codepoint[name])
        #print "Named ent:", c
    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        #print "Num ent  :", c
    def handle_decl(self, data):
        x = 5
        #print "Decl     :", data

    def printTuple(self):
        print self.classTuples


def getSchedule(url):
    page = urllib2.urlopen(url)
    content = page.read()
    parser = MyHTMLParser()
    parser.feed(content)
    parser.printTuple()



def main(argv):

    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    url = str(sys.argv[1])

    getSchedule(url)

	
if __name__ == "__main__":
    main(sys.argv[1:])
