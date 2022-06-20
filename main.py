from curses import def_shell_mode
from re import T
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
       for lines in csvFile:
        line = json.dumps(lines)
        x = line.rstrip().split(",")
        if (x[0] == '{"Report ID:": "===================================================================================================================================================================================="'):
            if (fc != 0):
                if (tl != 0):
                    yi.append(tl)
                    tl = 1
                else:
                    tl = 1
            else:
                fc = 1
        elif (tl > 0):
            if (x[0] == '{"Report ID:": "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"'):
                yi.append(tl)
                tl = 0
            else:
                tl += 1
# opening the CSV file to add all students and courses
with open(file_path, mode ='r') as file:   
        
       # reading the CSV file
       csvFile = csv.DictReader(file)
 
       # displaying the contents of the CSV file
       y = []
       l = 0
       c = 0
       for lines in csvFile:
            #print(lines)
            line = json.dumps(lines)
            x = line.rstrip().split(",")
            #print(x)
            if (x[0] == '{"Report ID:": "===================================================================================================================================================================================="'):
                 l = 1
            elif (l > 0):
                y.append(x)
                print(y[c])
                c += 1
                l += 1
                if (l == 2):
                    for c1 in range (0,5):
                        ns = x[c1].split(": ")
                        if (c1 == 0):
                            surname = ""
                            for nc in range (1, len(ns[1])):
                                surname = surname + ns[1][nc]
                                print(ns[1][nc],end="")
                            print(",",end="")
                        if (c1 == 1):
                            name = ""
                            for nc in range (0, len(ns[0])-4):
                                name = name + ns[0][nc]
                                print(ns[0][nc],end="")
                            print(",",end="")
                            sex = ""
                            for nc in range (len(ns[0])-3,len(ns[0])-1):
                                sex = sex + ns[0][nc]
                                print(ns[0][nc],end="")
                            print(",",end="")
                        if (c1 == 2):
                            stdno = ""
                            for nc in range (1, len(ns[1])-1):
                                stdno = stdno + ns[1][nc]
                                print(ns[1][nc],end="")
                            print(",",end="")
                        if (c1 == 3):
                            emplID = ""
                            for nc in range (1, len(ns[1])-1):
                                emplID = emplID + ns[1][nc]
                                print(ns[1][nc],end="")
                            print(",",end="")
                        if (c1 == 4):
                            prog = ""
                            for nc in range (1, len(ns[1])-1):
                                prog = prog + ns[1][nc]
                                print(ns[1][nc],end="")
                            print(",",end="")
                    print("")
                    std = student(stdno,name,surname,sex,emplID,prog)
                    stdarr.append(std)
                if (l == 4):
                    l = 0
                    for c1 in range (0,5):
                        ns = x[c1].split(": ")
                        if (c1 == 0):
                            for nc in range (1, len(ns[1])-1):
                                print(ns[1][nc],end="")
                            print(",",end="")
                        if (c1 == 2):
                            for nc in range (1, len(ns[1])-1):
                                print(ns[1][nc],end="")
                            print(",",end="")
                        if (c1 == 3):
                            for nc in range (1, len(ns[1])-1):
                                print(ns[1][nc],end="")
                            print(",",end="")
                        if (c1 == 4):
                            for nc in range (1, len(ns[1])-2):
                                print(ns[1][nc],end="")
                            print(",",end="")
                    print("")
                    #std = student()

print(stdarr[1].stdno)
for i in range(0,len(yi)):
    print(yi[i],end="")
    print(",",end="")
print("")

