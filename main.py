from pickle import FALSE, TRUE
import tkinter as tk
from tkinter import filedialog
import csv
import json

# Adding Classes objects for students and code which will be used in this App. 
# There is one for students and one for course, both related by the studno attribute which is common for both object classes
# One to many relationship between students and courses as one student can have many courses
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
# This ended up being redunandant as as now the method of determining year is based on gaging the first read of the file
# then re-reading it again to get the useful bits
yi = []


#Array for storing the core courses for each degree program
#These exclude any degree programs that require choice to work out
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
# Arrays for optional core courses
opcore_ECE_3 = ["CSC2002S","EEE3093S","EEE3094S"]
opcore_ECE3_taken = []
opcore_ECE_4 = ["EEE4114F","EEE4118F","EEE4120F","EEE4121F"]
opcore_ECE4_taken = []
opcore_EE_4 = ["EEE4115F","EEE4118F","EEE4121F"]
opcore_ME_4 = ["EEE4115F","EEE4118F","EEE4119F"]
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

# opening the CSV file to find out where everything is in relation to the students previous academic year
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

# opening the CSV file to add all students and courses to arrays storing each of their object classes
# Information found after the first reading is made useful here in only storing the most recent student GPA
with open(file_path, mode ='r') as file:   
        # reading the CSV file
        csvFile = csv.reader(file)
 
        # Initial state of key counter variables and flags for reading info
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
                if (l == 2): #Goal here is to poplate the variables that will be required to form the student object.
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
                                cyear = int(tyear) #First index of the array should contain a year if its not a year and its a "the following code won't execute"
                                #print(cyearArr[ind],cyear)
                                if (cyear < pyearArr[ind]): #if the year is before the previous term it creates a GPA in case the previous term has no GPA
                                    read = 1
                                    ns = x[18]
                                    spgpa = ""
                                    for nc in range (2, len(ns)-2):
                                        spgpa = spgpa + ns[nc]
                                elif (cyear == pyearArr[ind]): #If the year is the previous term then it adds the course and their mark for it
                                    read = 1
                                    ns = x[18]
                                    sgpa = ""
                                    for nc in range (2, len(ns)-2):
                                        sgpa = sgpa + ns[nc]
                                    if (cyear == 2020):
                                        igpa = float(spgpa)
                                    else:
                                        igpa = float(sgpa)
                                    std = student(stdno,name,surname,sex,emplID,prog,igpa,cyear) #Creating student object for student
                                    stdarr.append(std) #Adding object to student odject array
                                else: 
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

#Now that the contents of the csv files have been read this is where the data is manipulated.
QUIT = FALSE
while (QUIT == FALSE): #Program Loop which only ends when key 1 is entered.
    print("")
    print("Enter code for next operation")
    print("0 - Student Assessment")
    print("1 - Quit App")
    print("Enter code: ", end="")
    val_code = input()
    if (val_code == "0"): #Open if assess student is chosen
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
        opECE3_count = 0
        opECE4_count = 0
        cmissing = []
        core = FALSE
        cmissing_temp1 = [] # core courses failed initially
        cmissing_temp2 = [] # core courses passed on other attempts
        if (stdyear != ""): #To check if the year exists which will only be blank if the student number entered does not exist
            for i in range (0, len(carr)):
                that_year = carr[i].year
                if (student_no == carr[i].stdno): #Relating to courses the student did in the previously and whether they passed them
                    if (prog1 == "EB009"): #If degree program is Electrical Engineering
                        for k in range (0, len(core_EE)):
                            if (core_EE[k] == carr[i].courseCode):
                                core = TRUE
                        for l in range (0, len(opcore_EE_4)):
                            if (opcore_EE_4[l] == carr[i].courseCode):
                                core = TRUE
                    if (prog1 == "EB011"): #If degree program is Mechatronics
                        for k in range (0, len(core_ME)):
                            if (core_ME[k] == carr[i].courseCode):
                                core = TRUE
                    if (prog1 == "EB022"): #If degree program is Electrical and Computer Engineering
                        # for k in range (0,len(opcore_ECE3_taken)):
                        #     there = FALSE
                        #     for l in range (0, len(op))
                        for k in range (0, len(core_ECE)):
                            if (core_ECE[k] == carr[i].courseCode):
                                core = TRUE
                    if (that_year == stdyear):
                        ctotal += 1
                        if (carr[i].mark == "UP" or carr[i].mark == "PA"): #Student passed a (Supp exam, Prac course, 2020 course) 
                            cpassed += 1
                            if (prog1 == "EB022"):
                                for k in range (0,len(opcore_ECE_3)):
                                    if (carr[i].courseCode == opcore_ECE_3[k]): 
                                        opcore_ECE3_taken.append(carr[i].courseCode)
                                        opECE3_count += 1
                                for k in range (0,len(opcore_ECE_4)):
                                    if (carr[i].courseCode == opcore_ECE_4[k]): 
                                        opcore_ECE4_taken.append(carr[i].courseCode)
                                        opECE4_count += 1
                        elif(len(carr[i].mark) == 2): #Passed conventionally
                            try:
                                mark = int(carr[i].mark)
                                if (mark >= 50):
                                    cpassed += 1
                                    if (prog1 == "EB022"): #To check which of the three optional core ECE courses were taken (previous term)
                                        for k in range (0,len(opcore_ECE_3)):
                                            if (carr[i].courseCode == opcore_ECE_3[k]): 
                                                opcore_ECE3_taken.append(carr[i].courseCode)
                                                opECE3_count += 1
                                        for k in range (0,len(opcore_ECE_4)):
                                            if (carr[i].courseCode == opcore_ECE_4[k]): 
                                                opcore_ECE4_taken.append(carr[i].courseCode)
                                                opECE4_count += 1
                                else:
                                    if (core == TRUE): #If student did not pass core courses done in the previous term then it is added here
                                        cmissing.append(carr[i].courseCode)
                            except: #If mark is not an integer it is then ignored without breaking the app
                                cpassed = cpassed
                        else:
                            if (core == TRUE):
                                cmissing.append(carr[i].courseCode)
                    else:
                        if (carr[i].mark == "UP" or carr[i].mark == "PA"): #Student passed a (Supp exam, Prac course, 2020 course) 
                            cpassed = cpassed
                            if (prog1 == "EB022"): #To check which of the three optional core ECE courses were taken (all terms before previous)
                                for k in range (0,len(opcore_ECE_3)):
                                    if (carr[i].courseCode == opcore_ECE_3[k]): 
                                        opcore_ECE3_taken.append(carr[i].courseCode)
                                        opECE3_count += 1
                                for k in range (0,len(opcore_ECE_4)):
                                    if (carr[i].courseCode == opcore_ECE_4[k]): 
                                        opcore_ECE4_taken.append(carr[i].courseCode)
                                        opECE4_count += 1
                            if (carr[i].courseCode == "MAM1020F"): #Maths courses that can be taken as F/S
                                cmissing_temp2.append("MAM1020S")
                                cmissing_temp2.append(carr[i].courseCode)
                            elif (carr[i].courseCode == "MAM1020S"):
                                cmissing_temp2.append("MAM1020F")
                                cmissing_temp2.append(carr[i].courseCode)
                            elif (carr[i].courseCode == "MAM1021S"):
                                cmissing_temp2.append("MAM1021F")
                                cmissing_temp2.append(carr[i].courseCode)
                            elif (carr[i].courseCode == "MAM1021F"):
                                cmissing_temp2.append("MAM1021S")
                                cmissing_temp2.append(carr[i].courseCode)
                            elif (carr[i].courseCode == "MAM2083F"):
                                cmissing_temp2.append("MAM2083S")
                                cmissing_temp2.append(carr[i].courseCode)
                            elif (carr[i].courseCode == "MAM2083S"):
                                cmissing_temp2.append("MAM2083F")
                                cmissing_temp2.append(carr[i].courseCode)
                            elif (carr[i].courseCode == "MAM2084S"):
                                cmissing_temp2.append("MAM2084F")
                                cmissing_temp2.append(carr[i].courseCode)
                            elif (carr[i].courseCode == "MAM2084F"):
                                cmissing_temp2.append("MAM2084S")
                                cmissing_temp2.append(carr[i].courseCode)                          
                            elif (carr[i].courseCode == "PHY1012F"): #Physics courses that can be taken as F/S
                                cmissing_temp2.append("PHY1012S")
                                cmissing_temp2.append(carr[i].courseCode)
                            elif (carr[i].courseCode == "PHY1012S"):
                                cmissing_temp2.append("PHY1012F")
                                cmissing_temp2.append(carr[i].courseCode)
                            elif (carr[i].courseCode == "PHY1013S"):
                                cmissing_temp2.append("PHY1013F")
                                cmissing_temp2.append(carr[i].courseCode)
                            elif (carr[i].courseCode == "PHY1013F"):
                                cmissing_temp2.append("PHY1013S")
                                cmissing_temp2.append(carr[i].courseCode)
                            elif (carr[i].courseCode == "MEC1009S"): #MEC courses that can be taken as F/S
                                cmissing_temp2.append("MAM1009F")
                                cmissing_temp2.append(carr[i].courseCode)
                            elif (carr[i].courseCode == "MEC1009F"):
                                cmissing_temp2.append("MEC1009S")
                                cmissing_temp2.append(carr[i].courseCode)
                            else:
                                cmissing_temp2.append(carr[i].courseCode)
                        elif(len(carr[i].mark) == 2): #Passed conventionally
                            try:
                                mark = int(carr[i].mark)
                                if (mark >= 50):
                                    cpassed = cpassed
                                    if (prog1 == "EB022"):
                                        for k in range (0,len(opcore_ECE_3)):
                                            if (carr[i].courseCode == opcore_ECE_3[k]): 
                                                opcore_ECE3_taken.append(carr[i].courseCode)
                                                opECE3_count += 1
                                        for k in range (0,len(opcore_ECE_4)):
                                            if (carr[i].courseCode == opcore_ECE_4[k]): 
                                                opcore_ECE4_taken.append(carr[i].courseCode)
                                                opECE4_count += 1
                                    if (carr[i].courseCode == "MAM1020F"): #Maths courses that can be taken as F/S
                                        cmissing_temp2.append("MAM1020S")
                                        cmissing_temp2.append(carr[i].courseCode)
                                    elif (carr[i].courseCode == "MAM1020S"):
                                        cmissing_temp2.append("MAM1020F")
                                        cmissing_temp2.append(carr[i].courseCode)
                                    elif (carr[i].courseCode == "MAM1021S"):
                                        cmissing_temp2.append("MAM1021F")
                                        cmissing_temp2.append(carr[i].courseCode)
                                    elif (carr[i].courseCode == "MAM1021F"):
                                        cmissing_temp2.append("MAM1021S")
                                        cmissing_temp2.append(carr[i].courseCode)
                                    elif (carr[i].courseCode == "MAM2083F"):
                                        cmissing_temp2.append("MAM2083S")
                                        cmissing_temp2.append(carr[i].courseCode)
                                    elif (carr[i].courseCode == "MAM2083S"):
                                        cmissing_temp2.append("MAM2083F")
                                        cmissing_temp2.append(carr[i].courseCode)
                                    elif (carr[i].courseCode == "MAM2084S"):
                                        cmissing_temp2.append("MAM2084F")
                                        cmissing_temp2.append(carr[i].courseCode)
                                    elif (carr[i].courseCode == "MAM2084F"):
                                        cmissing_temp2.append("MAM2084S")
                                        cmissing_temp2.append(carr[i].courseCode)                          
                                    elif (carr[i].courseCode == "PHY1012F"): #Physics courses that can be taken as F/S
                                        cmissing_temp2.append("PHY1012S")
                                        cmissing_temp2.append(carr[i].courseCode)
                                    elif (carr[i].courseCode == "PHY1012S"):
                                        cmissing_temp2.append("PHY1012F")
                                        cmissing_temp2.append(carr[i].courseCode)
                                    elif (carr[i].courseCode == "PHY1013S"):
                                        cmissing_temp2.append("PHY1013F")
                                        cmissing_temp2.append(carr[i].courseCode)
                                    elif (carr[i].courseCode == "PHY1013F"):
                                        cmissing_temp2.append("PHY1013S")
                                        cmissing_temp2.append(carr[i].courseCode)
                                    elif (carr[i].courseCode == "MEC1009S"): #MEC courses that can be taken as F/S
                                        cmissing_temp2.append("MEC1009F")
                                        cmissing_temp2.append(carr[i].courseCode)
                                    elif (carr[i].courseCode == "MEC1009F"):
                                        cmissing_temp2.append("MEC1009S")
                                        cmissing_temp2.append(carr[i].courseCode)
                                    else:
                                        cmissing_temp2.append(carr[i].courseCode)
                                else:
                                    if (core == TRUE): #If student did not pass core courses done in the previous term then it is added here
                                        cmissing_temp1.append(carr[i].courseCode)
                            except: #If mark is not an integer it is then ignored without breaking the app
                                cpassed = cpassed
                        else:
                            if (core == TRUE):
                                cmissing_temp1.append(carr[i].courseCode)
            for count in range (0,len(cmissing_temp1)): #This is to check if anything in cmissing 1 is in cmissing 2. If any course failed was evenually passed
                there = FALSE
                for count1 in range (0, len(cmissing_temp2)):
                    if (cmissing_temp1[count] == cmissing_temp2[count1]):
                        there = TRUE
                if (there == FALSE):
                    cmissing.append(cmissing_temp1[count])
            if (prog1 == "EB022"):
                if (len(opcore_ECE3_taken) < 2):
                    for count in range (0,len(opcore_ECE_3)):
                        there = FALSE
                        for count1 in range (0, len(opcore_ECE3_taken)):
                            if (opcore_ECE_3[count] == opcore_ECE3_taken[count1]):
                                there = TRUE
                        if (there == FALSE):
                            cmissing.append(opcore_ECE_3[count])
                # if (len(opcore_ECE4_taken) < 2):
                #     for count in range (0,len(opcore_ECE_4)):
                #         there = FALSE
                #         for count1 in range (0, len(opcore_ECE4_taken)):
                #             if (opcore_ECE_4[count] == opcore_ECE4_taken[count1]):
                #                 there = TRUE
                #         if (there == FALSE):
                #             cmissing.append(opcore_ECE_4[count])
            print("Number of courses passed in previous term: ",cpassed)
            print("Number of courses taken in previous term: ",ctotal)
            if (cpassed > 5 and cpassed < 7):
                print("Recommendation is to take fewer courses each semester. To a maximum of 4 courses eeach semester")
            elif (cpassed >= 7):
                print("No recommendations can proceed unhindered")
            if (prog1 == "EB009"): #This is to ensure that core courses that were not done are added to the not done pile
                for lm in range (0, len(core_EE)):
                    there = FALSE
                    for ln in range (0, len(carr)):
                        if (carr[ln].courseCode == core_EE[lm]):
                            there = TRUE
                    if (there == FALSE):
                        cmissing.append(core_EE[lm])
                for lm in range (0, len(opcore_EE_4)):
                    there = FALSE
                    for ln in range (0, len(carr)):
                        if (carr[ln].courseCode == opcore_EE_4[lm]):
                            there = TRUE
                    if (there == FALSE):
                        cmissing.append(opcore_EE_4[lm])
            elif (prog1 == "EB011"):
                for lm in range (0, len(core_ME)):
                    there = FALSE
                    for ln in range (0, len(carr)):
                        if (carr[ln].courseCode == core_ME[lm]):
                            there = TRUE
                    if (there == FALSE):
                        cmissing.append(core_ME[lm])
                for lm in range (0, len(opcore_ME_4)):
                    there = FALSE
                    for ln in range (0, len(carr)):
                        if (carr[ln].courseCode == opcore_ME_4[lm]):
                            there = TRUE
                    if (there == FALSE):
                        cmissing.append(opcore_ME_4[lm])
            elif (prog1 == "EB022"):
                for lm in range (0, len(core_ECE)):
                    there = FALSE
                    for ln in range (0, len(carr)):
                        if (carr[ln].courseCode == core_ECE[lm]):
                            there = TRUE
                    if (there == FALSE):
                        cmissing.append(core_ECE[lm])
                for lm in range (0, len(opcore_ECE_4)):
                    there = FALSE
                    for ln in range (0, len(carr)):
                        if (carr[ln].courseCode == opcore_ECE_4[lm]):
                            there = TRUE
                    if (there == FALSE):
                        cmissing.append(opcore_ECE_4[lm])
            print("The core courses yet to be completed for the",prog1,"degree program for",student_no,"are:")
            for l in range (0,len(cmissing)):
                print(cmissing[l])
        else:
            print("")
            print("Unfortunately this student does not exist")
    elif (val_code == "1"): #The option to exit the program is used.
        QUIT = TRUE
    else:
        print("")
        print("That code des not exist, please try again!")
print("")
print("Thank you for using the application")

