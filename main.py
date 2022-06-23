#from curses import def_shell_mode
#from re import T
import tkinter as tk
from tkinter import filedialog
import csv
import json

class student:
    def __init__(self, stdno, name, surname, sex, emplID, Prog):
        self.stdno = stdno
        self.name = name
        self.surname = surname
        self.sex = sex
        self.emplID = emplID
        self.Prog = Prog
class course: 
    def __init__(self, courseCode, name, passRate, stdno):
        self.courseCode = courseCode
        self.name = name
        self.passRate = passRate
        self.stdno = stdno

#Creating the arrays the hold the student objects and the course objects
stdarr = []
carr = []
# Array required for finding out lengths of individual student records
yi = []
# Array for storing latest year on transript info
cyearArr = []

# Required for creating the Dialog Box
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
 
# opening the CSV file to find out where everything is
with open(file_path, mode ='r') as file:   
       # reading the CSV file
       csvFile = csv.DictReader(file)
       tl = 0
       fc = 0
       cyear = 0
       for lines in csvFile:
        line = json.dumps(lines)
        x = line.rstrip().split(",")
        if (x[0] == '{"Report ID:": "===================================================================================================================================================================================="'):
            if (fc != 0):
                if (tl != 0):
                    yi.append(tl)
                    cyearArr.append(pyear)
                    cyear = 0
                    pyear = 0
                    tl = 1
                else:
                    tl = 1
                    cyear = 0
                    pyear = 0
            else:
                fc = 1
        elif (tl > 0):
            ns = x[0].split(": ")
            if (tl == 3):
                tyear = ""
                for nc in range (1,len(ns[1])-1):
                    tyear += ns[1][nc]
                cyear = int(tyear)       
            elif (tl > 4):
                tyear = ""
                for nc in range (1,len(ns[1])-1):
                    tyear += ns[1][nc]
                try:
                    if (int(tyear) > cyear):
                        pyear = cyear
                        cyear = int(tyear)
                except:
                    tl = tl
            if (x[0] == '{"Report ID:": "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"'):
                yi.append(tl)
                cyearArr.append(pyear)
                tl = 0
            else:
                tl += 1
# opening the CSV file to add all students and courses
with open(file_path, mode ='r') as file:   
        
       # reading the CSV file
       csvFile = csv.reader(file)
 
       # displaying the contents of the CSV file
       y = []
       l = 0
       c = 0
       fc = 0
       ind = 0
       read = 0
       for lines in csvFile:
            #print(lines)
            line = json.dumps(lines)
            x = line.rstrip().split(",")
            #print(x[0])
            if (x[0] == '["===================================================================================================================================================================================="'):
                if (fc != 0):
                    l = 1
                else:
                    fc = 1
            elif (l > 0):
                y.append(x)
                #print(y[c])
                c += 1
                l += 1
                if (l == 2):
                    if(c > 2):
                        print("")
                    for c1 in range (0,5):
                        ns = x[c1]
                        if (c1 == 0):
                            surname = ""
                            for nc in range (2, len(ns)):
                                surname = surname + ns[nc]
                                print(ns[nc],end="")
                            print(",",end="")
                        if (c1 == 1):
                            name = ""
                            for nc in range (0, len(ns)-4):
                                name = name + ns[nc]
                                print(ns[nc],end="")
                            print(",",end="")
                            sex = ""
                            for nc in range (len(ns)-3,len(ns)-1):
                                sex = sex + ns[nc]
                                print(ns[nc],end="")
                            print(",",end="")
                        if (c1 == 2):
                            stdno = ""
                            for nc in range (2, len(ns)-1):
                                stdno = stdno + ns[nc]
                                print(ns[nc],end="")
                            print(",",end="")
                        if (c1 == 3):
                            emplID = ""
                            for nc in range (2, len(ns)-1):
                                emplID = emplID + ns[nc]
                                print(ns[nc],end="")
                            print(",",end="")
                        if (c1 == 4):
                            prog = ""
                            for nc in range (2, len(ns)-1):
                                prog = prog + ns[nc]
                                print(ns[nc],end="")
                            print(",",end="")
                    print("")
                    std = student(stdno,name,surname,sex,emplID,prog)
                    stdarr.append(std)
                elif (l > 3):
                    for c1 in range (0,5):
                        ns = x[c1]
                        ns1 = x[1]
                        #print(ns1)
                        if (c1 == 0):
                            tyear = ""
                            for nc in range (2,len(ns)-1):
                                tyear += ns[nc]
                            try:
                                cyear = int(tyear)
                                #print(cyearArr[ind],cyear)
                                if (cyear == cyearArr[ind]):
                                    read = 1
                                    ns = x[4]
                                    sgpa = ""
                                    for nc in range (1, len(ns)-1):
                                        sgpa = sgpa + ns[nc]
                                    igpa = int(sgpa)
                                elif(cyear > cyearArr[ind]):
                                    read = 0
                                    ind += 1
                            except:
                                l = l
                        if (c1 == 1 and read == 1 and len(ns1) == 11):
                            nsp = x[0] 
                            if (nsp == '[""'):
                                courseC = ""
                                for nc in range (2, len(ns)-1):
                                    courseC = courseC + ns[nc]
                                    print(ns[nc],end="")
                                print(",",end="")
                        if (c1 == 2 and read == 1 and len(ns1) == 11):
                            nsp = x[0] 
                            if (nsp == '[""'):
                                mark = ""
                                for nc in range (2, len(ns)-1):
                                    mark = mark + ns[nc]
                                    print(ns[nc],end="")
                                print(",",end="")
                        if (c1 == 9 and read == 1 and len(ns1) == 11):
                            nsp = x[0]
                            if (nsp == '[""'):
                                courseC2 = ""
                                for nc in range (1, len(ns[1])-1):
                                    courseC2 = courseC2 + ns[nc]
                                    print(ns[nc],end="")
                                print(",",end="")
                        
print("")
# print(stdarr[1].stdno)
# for i in range(0,len(yi)):
#     print(yi[i],"",cyearArr[i],end="")
#     print(",",end="")
# print("")

