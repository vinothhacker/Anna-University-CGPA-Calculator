def gradepoints(grade):

    points = 0
    if grade == 'O' or grade == 'o':
        points += 10
        return points
    if grade == 'A+' or grade == 'a+':
        points += 9
        return points
    if grade == 'A' or grade == 'a':
        points += 8
        return points
    if grade == 'B+' or grade == 'b+':
        points += 7
        return points
    if grade == 'B' or grade == 'b':
        points += 6
        return points
    if grade == 'U' or grade == 'u':
        points += 0
        return points


def checkInputValue(subcode, subcredit, subName):
     while True:
        try:
            subcode = float(gradepoints(input("Enter Your Grade For " + subName)))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
     subcode = subcode * subcredit
     return subcode


def gpacalsem1():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 1....\n")

    hs8151 = checkInputValue("hs8151", 4, "Communicative English (HS8151) :")
    ma8151 = checkInputValue("ma8151", 4, "Engineering Mathematics - 1(MA8151) :")
    ph8151 = checkInputValue("ph8151", 3, "Engineering Physics (PH8151) :")
    cy8151 = checkInputValue("cy8151", 3, "Engineering Chemistry (CY8151) :")
    ge8151 = checkInputValue("ge8151", 3, "Problem Solving and Python Programming (GE8151) :")
    ge8152 = checkInputValue("ge8152", 4, "Engineering Graphics (GE8152) :")
    ge8161 = checkInputValue("ge8161", 2, "PSPP Laboratory (GE8161) :")
    bs8161 = checkInputValue("bs8161", 2, "Physics and Chemistry Lab (BS8161) :")

    firstSemGpa = float((hs8151 + ma8151 + ph8151 + cy8151 + ge8151 + ge8161 + ge8152 + bs8161)) / 25
    print("\nYour First Semester GPA is ", round(firstSemGpa, 2))
    return firstSemGpa


def gpacalsem2():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 2....\n")

    hs8251 = checkInputValue("hs8251", 4, "Technical English (HS8251) :")
    ma8251 = checkInputValue("ma8251", 4, "Engineering Mathematics - 2(MA8251) :")
    ph8253 = checkInputValue("ph8253", 3, "Physics For Electronics Engineering (PH8253) :")
    be8254 = checkInputValue("be8254", 3, "Basic Electrical and Instrumentation Engineering (BE8254) :")
    ec8251 = checkInputValue("ec8251", 4, "Circuit Analysis (EC8251) :")
    ec8252 = checkInputValue("ec8252", 3, "Electronic Devices (EC8252) :")
    ec8261 = checkInputValue("ec8261", 2, "Circuits and Devices Laboratory (GE8161) :")
    ge8261 = checkInputValue("ge8261", 2, "Engineering Practices Lab (BS8151) :")

    secSemGpa = float((hs8251 + ma8251 + ph8253 + be8254 + ec8251 + ec8252 + ec8261 + ge8261)) / 25
    print("\nYour Second Semester GPA is ", round(secSemGpa, 2))
    return secSemGpa


def gpacalsem3():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 3....\n")
    ma8352 = checkInputValue("ma8352", 4, "Linear Algebra and Partial Diff Equations (MA8352) :")
    ec8393 = checkInputValue("ec8393", 3, "Fundamentals of Data Structures In C (EC8393) :")
    ec8351 = checkInputValue("ec8351", 3, "Electronic Circuits-1 (EC8351) :")
    ec8352 = checkInputValue("ec8351", 4, "Signals And Systems(EC8352) :")
    ec8392 = checkInputValue("ec8392", 3, "Digital Electronics (EC8392) :")
    ec8391 = checkInputValue("ec8391", 3, "Control Systems Engineering (EC8391) :")
    ec8381 = checkInputValue("ec8381", 2, "FDS in C Laboratory (GE8161) :")
    ec8361 = checkInputValue("ec8361", 2, "Analog and Digital Circuits Lab (BS8151) :")
    hs8381 = checkInputValue("hs8381", 1, "Interpersonal Skills/Listening & Speaking (HS8381) :")

    thirdSemGpa = float((ma8352 + ec8393 + ec8351 + ec8352 + ec8392 + ec8391 + ec8381 + hs8381 + ec8361)) / 25
    print("\nYour Third Semester GPA is ", round(thirdSemGpa, 2))
    return thirdSemGpa


def gpacalsem4():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 4....\n")

    ma8451 = checkInputValue("ma8451", 4, "Probability and Random Processes (MA8451) :")
    ec8452 = checkInputValue("ec8452", 3, "Electronic Circuits-2 (EC8452) :")
    ec8491 = checkInputValue("ec8491", 3, "Communication Theory (EC8491) :")
    ec8451 = checkInputValue("ec8451", 4, "Electromagnetic Fields (EC8451) :")
    ec8453 = checkInputValue("ec8453", 3, "Linear Integrated Circuits (EC8453) :")
    ge8291 = checkInputValue("ge8291", 3, "Environmental Science and Engineering (GE8291) :")
    ec8461 = checkInputValue("ec8461", 2, "Circuits Design and Simulation Laboratory (EC8461) :")
    ec8462 = checkInputValue("ec8462", 2, "Linear Integrated Circuits Laboratory (EC8462) :")

    fourSemGpa = float((ma8451 + ec8452 + ec8491 + ec8451 + ec8453 + ge8291 + ec8461 + ec8462)) / 24
    print("\nYour Fourth Semester GPA is ", round(fourSemGpa, 2))
    return fourSemGpa


def gpacalsem5():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 5....\n")
    ec8501 = checkInputValue("ec8501", 3, "Digital Communication (EC8501) :")
    ec8553 = checkInputValue("ec8553", 4, "Discrete-Time Signal Processing (EC8553) :")
    ec8552 = checkInputValue("ec8552", 3, "Computer Architecture and Organization (EC8552 :")
    ec8551 = checkInputValue("ec8551", 3, "Communication Networks (EC8551) :")
    pe1 = checkInputValue("pe1", 3, "Professional Elective 1  :")
    oe1 = checkInputValue("oe1", 3, "Open Elective 1  :")
    ec8562 = checkInputValue("ec8562", 2, "Digital Signal Processing Laboratory (EC8562) :")
    ec8561 = checkInputValue("ec8561", 2, "Communications System Laboratory (EC8561) :")
    ec8563 = checkInputValue("ec8563", 2, "Communications Networks Laboratory (EC8561) :")

    fiveSemGpa = float((ec8501 + ec8553 + ec8552 + ec8551 + oe1 + pe1 + ec8562 + ec8563 + ec8561)) / 25
    print("\nYour Fifth Semester GPA is ", round(fiveSemGpa, 2))
    return fiveSemGpa


def gpacalsem6():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 6....\n")

    ec8691 = checkInputValue("ec8691", 3, "Microprocessors and Microcontrollers (EC8691) :")
    ec8095 = checkInputValue("ec8095", 3, "VLSI Design (EC8095) :")
    ec8652 = checkInputValue("ec8652", 3, "Wireless Communication (EC8652) :")
    mg8591 = checkInputValue("mg8591", 3, "Principles of Management (MG8591) :")
    ec8651 = checkInputValue("ec8651", 3, "Transmission Lines and RF Systems (EC8651)  :")
    pe2 = checkInputValue("pe2", 3, "Professional Elective 2  :")
    ec8681 = checkInputValue("ec8681", 2, "MPMC Laboratory  :")
    ec8661 = checkInputValue("ec8661", 2, "VLSI Design Laboratory (EC8661) :")
    ec8611 = checkInputValue("ec8611", 1, "Technical Seminar (EC8611) :")

    sixSemGpa = float((ec8691 + ec8095 + ec8652 + mg8591 + ec8651 + pe2 + ec8681 + ec8661 + ec8611)) / 23
    print("\nYour Sixth Semester GPA is ", round(sixSemGpa, 2))
    return sixSemGpa


def gpacalsem7():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 7....\n")

    ec8701 = checkInputValue("ec8701", 3, "Antennas and Microwave (EC8701) :")
    ec8751 = checkInputValue("ec8751", 3, "Optical Communication (EC8751) :")
    ec8791 = checkInputValue("ec8791", 3, "Embedded and Real Time Systems (EC8791) :")
    ec8702 = checkInputValue("ec8702", 3, "Ad hoc and Wireless Sensor Networks (EC8702) :")
    pe3 = checkInputValue("pe3", 3, "Professional Elective 3  :")
    oe2 = checkInputValue("oe2", 3, "Open Elective 2  :")
    ec8711 = checkInputValue("ec8711", 2, "Embedded Laboratory (EC8711) :")
    ec8761 = checkInputValue("ec8761", 2, "Advanced Communication Laboratory (EC8561) :")

    sevenSemGpa = float((ec8701 + ec8751 + ec8791 + ec8702 + pe3 + oe2 + ec8711 + ec8761)) / 22
    print("\nYour Seventh Semester GPA is ", round(sevenSemGpa, 2))
    return sevenSemGpa

def gpacalsem8():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 8....\n")

    pe4 = checkInputValue("pe4", 3, "Professional Elective 4  :")
    pe5 = checkInputValue("pe5", 3, "Professional Elective 5  :")
    ec8761 = checkInputValue("ec8761", 10, "Project Work :")

    eightSemGpa = float((pe4 + pe5 + ec8761)) / 16
    print("\nYour Eighth Semester GPA is ", round(eightSemGpa, 2))
    return eightSemGpa

def gpacalallsem():
    print("\nCALCULATING YOUR CGPA FOR ALL SEMESTERS ....\n")

    seme1 = gpacalsem1()
    seme2 = gpacalsem2()
    seme3 = gpacalsem3()
    seme4 = gpacalsem4()
    seme5 = gpacalsem5()
    seme6 = gpacalsem6()
    seme7 = gpacalsem7()
    seme8 = gpacalsem8()
    cgpa = (seme1 + seme2 + seme3 + seme4 + seme5 + seme6 + seme7 + seme8) / 8
    print("Your Cumulative Grade Point Average is ", round(cgpa, 2))

print("* * * Anna University CGPA || GPA Calculator * * *\n")

input("Press Enter to continue...")
print("\nBranch Of Study : Electronics and Communication Engineering \n")
while True:
    try:
        gpaorcgpa = int(input("Press 0 For Calculating GPA || Press 1 For Calculating CGPA :"))
        if 0 <= gpaorcgpa <= 1:
            break
        raise ValueError()
    except ValueError:
        print("Invalid Input Please Enter 0 Or 1 !!!")

if gpaorcgpa == 0:
    while True:
        try:
            semester = int(input("Enter The Semester Number That You Want To Calculate GPA :"))
            if 0 <= semester <= 8:
                break
            raise ValueError()
        except ValueError:
            print("Invalid Input Please Enter a Number Between 0 to 8")

    if semester == 0:
        gpacalallsem()

    elif semester == 1:
        sem1 = gpacalsem1()

    elif semester == 2:
        sem2 = gpacalsem2()

    if semester == 3:
        sem3 = gpacalsem3()

    if semester == 4:
        sem4 = gpacalsem4()

    if semester == 5:
        sem5 = gpacalsem5()

    if semester == 6:
        sem6 = gpacalsem6()

    if semester == 7:
        sem7 = gpacalsem7()

    if semester == 8:
        sem8 = gpacalsem8()
if gpaorcgpa == 1:
    print("Enter 0 For Calculating CGPA For All Semesters.....\n")
    while True:
        try:
            untillsemx = int(input("Enter The Number Of Semesters That You Want to Calculate CGPA..."))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        except ValueError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break

    if untillsemx == 0:
        gpacalallsem()

    elif untillsemx == 1:
        print("\nCALCULATING YOUR CGPA FOR ONE SEMESTER ....\n")
        seme1 = gpacalsem1()
        cgpa = seme1
        print("\nYour Cumulative Grade Point Average is ", round(cgpa, 2))
    elif untillsemx == 2:
        print("\nCALCULATING YOUR CGPA FOR TWO SEMESTERS ....\n")
        seme1 = gpacalsem1()
        seme2 = gpacalsem2()
        cgpa = (seme1 + seme2) / 2
        print("\nYour Cumulative Grade Point Average is ", round(cgpa, 2))
    elif untillsemx == 3:
        print("\nCALCULATING YOUR CGPA FOR THREE SEMESTERS ....\n")
        seme1 = gpacalsem1()
        seme2 = gpacalsem2()
        seme3 = gpacalsem3()
        cgpa = (seme1 + seme2 + seme3) / 3
        print("\nYour Cumulative Grade Point Average is ", round(cgpa, 2))
    elif untillsemx == 4:
        print("\nCALCULATING YOUR CGPA FOR FOUR SEMESTERS ....\n")
        seme1 = gpacalsem1()
        seme2 = gpacalsem2()
        seme3 = gpacalsem3()
        seme4 = gpacalsem4()
        cgpa = (seme1 + seme2 + seme3 + seme4) / 4
        print("\nYour Cumulative Grade Point Average is ", round(cgpa, 2))
    elif untillsemx == 5:
        print("\nCALCULATING YOUR CGPA FOR FIVE SEMESTERS ....\n")
        seme1 = gpacalsem1()
        seme2 = gpacalsem2()
        seme3 = gpacalsem3()
        seme4 = gpacalsem4()
        seme5 = gpacalsem5()
        cgpa = (seme1 + seme2 + seme3 + seme4 + seme5) / 5
        print("\nYour Cumulative Grade Point Average is ", round(cgpa, 2))
    elif untillsemx == 6:
        print("\nCALCULATING YOUR CGPA FOR SIX SEMESTERS ....\n")
        seme1 = gpacalsem1()
        seme2 = gpacalsem2()
        seme3 = gpacalsem3()
        seme4 = gpacalsem4()
        seme5 = gpacalsem5()
        seme6 = gpacalsem6()
        cgpa = (seme1 + seme2 + seme3 + seme4 + seme5 + seme6) / 6
        print("\nYour Cumulative Grade Point Average is ", round(cgpa, 2))
    elif untillsemx == 7:
        print("\nCALCULATING YOUR CGPA FOR SEVEN SEMESTERS ....\n")
        seme1 = gpacalsem1()
        seme2 = gpacalsem2()
        seme3 = gpacalsem3()
        seme4 = gpacalsem4()
        seme5 = gpacalsem5()
        seme6 = gpacalsem6()
        seme7 = gpacalsem7()
        cgpa = (seme1 + seme2 + seme3 + seme4 + seme5 + seme6 + seme7) / 7
        print("\nYour Cumulative Grade Point Average is ", round(cgpa, 2))
    elif untillsemx == 8:
        gpacalallsem()

""" GPA = Sum of products of Grade Point of each subject in a semester and credits of
    corresponding subjects in a semester / Sum of credits in a semester"""















