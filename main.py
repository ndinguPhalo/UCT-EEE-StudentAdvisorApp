from pickle import FALSE, TRUE
import tkinter as tk
from tkinter import filedialog
import csv
import json

class student:
    def __init__(self, stdno, name, surname, sex, emplID, Prog, gpa, pyear):
        self.stdno = stdno
        self.name = name
        self.surname = surname
        self.sex = sex
        self.emplID = emplID
        self.Prog = Prog
        self.gpa = gpa
        self.pyear = pyear
class course: 
    def __init__(self, courseCode, mark, passRate, stdno, year):
        self.courseCode = courseCode
        self.mark = mark
        self.passRate = passRate
        self.stdno = stdno
        self.year = year

#Creating the arrays the hold the student objects and the course objects
stdarr = []
carr = []
# Array required for finding out lengths of individual student records
yi = []
#Array for storing the core courses for each degree program
core_ECE = ["EEE1006F","MAM1020F","CSC1015F","PHY1012F","MEC1003F","MAM1021S","PHY1013S","EEE1007S","CSC1016S","AXL1200S",
            "MEC1009F","EEE2045F","EEE2046F","EEE2048F","MAM2083F","EEE2047S","CON2026S","EEE2044S","PHY2010S","MAM2084S",
            "EEE3092F","EEE3090F","EEE3088F","EEE3089F","CSC2001F","EEE3096S","EEE3097S",
            "EEE4113F","CML4607F","EEE4022S","EEE4124C","EEE4125C",
            "EEE1000X","EEE3000X"] 
core_ME =  ["EEE1006F","MAM1020F","CSC1015F","PHY1012F","MEC1003F","MAM1021S","PHY1013S","EEE1007S","CSC1016S","AXL1200S",
            "MEC1009F","EEE2045F","EEE2046F","EEE2048F","MAM2083F","EEE2047S","CON2026S","EEE2044S","PHY2010S","MAM2084S",
            "EEE3092F","EEE3090F","EEE3088F","MEC2047F","EEE3091F","EEE3096S","MEC2045S","EEE3094S","EEE3099S",
            "EEE4113F","CML4607F","EEE4022S","EEE4124C","EEE4125C",
            "EEE1000X","EEE3000X"] 
core_EE =  ["EEE1006F","MAM1020F","CSC1015F","PHY1012F","MEC1003F","MAM1021S","PHY1013S","EEE1007S","CSC1016S","AXL1200S",
            "MEC1009F","EEE2045F","EEE2046F","EEE2048F","MAM2083F","EEE2047S","CON2026S","EEE2044S","PHY2010S","MAM2084S",
            "EEE3092F","EEE3090F","EEE3088F","EEE3089F","EEE3091F","EEE3093S","EEE3094S","EEE3098S","EEE3100S",
            "EEE4113F","CML4607F","EEE4022S","EEE4124C","EEE4125C",
            "EEE1000X","EEE3000X"] 
# Array for Missing Core courses
missingCoreArr = []
# Array for storing latest year on transript info
cyearArr = []
pyearArr = []

# Required for creating the Dialog Box
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
 
# Atrributes for students
surname = ""
name = ""
sex = ""
stdno = ""
emplID = ""
prog = ""

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
                    pyearArr.append(cyear)
                    cyearArr.append(cyear)
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
                pyearArr.append(pyear)
                cyearArr.append(cyear)
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
                    # if(c > 2):
                    #     print("")
                    for c1 in range (0,5):
                        ns = x[c1]
                        if (c1 == 0):
                            surname = ""
                            for nc in range (2, len(ns)):
                                surname = surname + ns[nc]
                            #     print(ns[nc],end="")
                            # print(",",end="")
                        if (c1 == 1):
                            name = ""
                            for nc in range (0, len(ns)-4):
                                name = name + ns[nc]
                            #     print(ns[nc],end="")
                            # print(",",end="")
                            sex = ""
                            for nc in range (len(ns)-3,len(ns)-1):
                                sex = sex + ns[nc]
                            #     print(ns[nc],end="")
                            # print(",",end="")
                        if (c1 == 2):
                            stdno = ""
                            for nc in range (2, len(ns)-1):
                                stdno = stdno + ns[nc]
                            #     print(ns[nc],end="")
                            # print(",",end="")
                        if (c1 == 3):
                            emplID = ""
                            for nc in range (2, len(ns)-1):
                                emplID = emplID + ns[nc]
                            #     print(ns[nc],end="")
                            # print(",",end="")
                        if (c1 == 4):
                            prog = ""
                            for nc in range (2, len(ns)-1):
                                prog = prog + ns[nc]
                    #             print(ns[nc],end="")
                    #         print(",",end="")
                    # print("")
                elif (l > 3):
                    for c1 in range (0,10):
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
                                if (cyear < pyearArr[ind]):
                                    read = 1
                                    ns = x[18]
                                    spgpa = ""
                                    for nc in range (2, len(ns)-2):
                                        spgpa = spgpa + ns[nc]
                                elif (cyear == pyearArr[ind]):
                                    read = 1
                                    ns = x[18]
                                    sgpa = ""
                                    for nc in range (2, len(ns)-2):
                                        sgpa = sgpa + ns[nc]
                                    if (cyear == 2020):
                                        igpa = float(spgpa)
                                    else:
                                        igpa = float(sgpa)
                                    std = student(stdno,name,surname,sex,emplID,prog,igpa,cyear)
                                    stdarr.append(std)
                                else: #elif(cyear > pyearArr[ind]):
                                    read = 0
                                    ind += 1
                            except:
                                l = l
                        if (read == 1 and len(ns) == 11):
                            nsp = x[0]
                            if (nsp == '[""'):
                                courseC = ""
                                for nc in range (2, len(ns)-1):
                                    courseC = courseC + ns[nc]
                                #     print(ns[nc],end="")
                                # print(",",end="")
                                ns = x[c1+1]
                                mark = ""
                                for nc in range (2, len(ns)-1):
                                    mark = mark + ns[nc]
                                #     print(ns[nc],end="")
                                # print(",",end="")
                                co = course(courseC,mark,50,stdno,cyear) 
                                carr.append(co)                    
print("The contents of file chosen have been read!")
QUIT = FALSE
while (QUIT == FALSE):
    print("")
    print("Enter code for next operation")
    print("0 - Student Assessment")
    print("1 - Quit App")
    print("Enter code: ", end="")
    val_code = input()
    if (val_code == "0"):
        print("Enter the student number of the student to be accessed: ", end="")
        student_no = input()
        stdyear = ""
        prog1 = ""
        for i in range (0,len(stdarr)):
            if (student_no == stdarr[i].stdno):
                print("GPA: ",stdarr[i].gpa)
                stdyear = stdarr[i].pyear
                prog1 = stdarr[i].Prog     
        cpassed = 0
        ctotal = 0
        that_year = 0
        cmissing = []
        core = FALSE
        if (stdyear != ""):
            for i in range (0, len(carr)):
                that_year = carr[i].year
                if (student_no == carr[i].stdno) and (that_year == stdyear):
                    ctotal += 1
                    if (prog1 == "EB009"):
                        for k in range (0, len(core_EE)):
                            if (core_EE[k] == carr[i].courseCode):
                                core = TRUE
                    if (prog1 == "EB011"):
                        for k in range (0, len(core_ME)):
                            if (core_ME[k] == carr[i].courseCode):
                                core = TRUE
                    if (prog1 == "EB022"):
                        for k in range (0, len(core_ECE)):
                            if (core_ECE[k] == carr[i].courseCode):
                                core = TRUE
                    if (carr[i].mark == "UP" or carr[i].mark == "PA"):
                        cpassed += 1
                    elif(len(carr[i].mark) == 2):
                        try:
                            mark = int(carr[i].mark)
                            if (mark >= 50):
                                cpassed += 1
                            else:
                                if (core == TRUE):
                                    cmissing.append(carr[i].courseCode)
                        except:
                            cpassed = cpassed
                    else:
                        if (core == TRUE):
                            cmissing.append(carr[i].courseCode)
            print("Number of courses passed in previous term: ",cpassed)
            print("Number of courses taken in previous term: ",ctotal)
            if (cpassed > 5 and cpassed < 7):
                print("Recommendation is to take fewer courses each semester. To a maximum of 4 courses eeach semester")
            elif (cpassed >= 7):
                print("No recommendations can proceed unhindered")
            if (prog1 == "EB009"):
                for lm in range (0, len(core_EE)):
                    there = FALSE
                    for ln in range (0, len(carr)):
                        if (carr[ln].courseCode == core_EE[lm]):
                            there = TRUE
                    if (there == FALSE):
                        cmissing.append(core_EE[lm])
            elif (prog1 == "EB011"):
                for lm in range (0, len(core_ME)):
                    there = FALSE
                    for ln in range (0, len(carr)):
                        if (carr[ln].courseCode == core_ME[lm]):
                            there = TRUE
                    if (there == FALSE):
                        cmissing.append(core_ME[lm])
            elif (prog1 == "EB022"):
                for lm in range (0, len(core_ECE)):
                    there = FALSE
                    for ln in range (0, len(carr)):
                        if (carr[ln].courseCode == core_ECE[lm]):
                            there = TRUE
                    if (there == FALSE):
                        cmissing.append(core_ECE[lm])
            print("The core courses yet to be completed for the",prog1,"degree program for",student_no,"are:")
            for l in range (0,len(cmissing)):
                print(cmissing[l])
        else:
            print("")
            print("Unfortunately this student does not exist")
    elif (val_code == "1"):
        QUIT = TRUE
    else:
        print("That code des not exist, please try again!")
print("Thank you for using the application")
# print(stdarr[2].stdno)
# for i in range(0,len(yi)):
#     print(yi[i],"",pyearArr[i],"",carr[i].stdno,end="")
#     print(",",end="")
# print("")

