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


def gpacalsem1():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 1....\n")

    while True:
        try:
            hs8151 = float(gradepoints(input("Enter Your Grade For Communicative English (HS8151) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    hs8151 = hs8151 * 4

    while True:
        try:
            ma8151 = float(gradepoints(input("Enter Your Grade For Engineering Mathematics - 1(MA8151) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ma8151 = ma8151 * 4

    while True:
        try:
            ph8151 = float(gradepoints(input("Enter Your Grade For Engineering Physics (PH8151) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ph8151 = ph8151 * 3

    while True:
        try:
            cy8151 = float(gradepoints(input("Enter Your Grade For Engineering Chemistry (CY8151) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    cy8151 = cy8151 * 3

    while True:
        try:
            ge8151 = float(gradepoints(input("Enter Your Grade For Problem Solving and Python Programming (GE8151) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ge8151 = ge8151 * 3

    while True:
        try:
            ge8152 = float(gradepoints(input("Enter Your Grade For Engineering Graphics (GE8152) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ge8152 = ge8152 * 4

    while True:
        try:
            ge8161 = float(gradepoints(input("Enter Your Grade For Problem Solving and Python Programming Laboratory (GE8161) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ge8161 = ge8161 * 2

    while True:
        try:
            bs8161 = float(gradepoints(input("Enter Your Grade For Physics and Chemistry Lab (BS8161) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    bs8161 = bs8161 * 2

    firstSemGpa = float((hs8151 + ma8151 + ph8151 + cy8151 + ge8151 + ge8161 + ge8152 + bs8161)) / 25
    print("\nYour First Semester GPA is ", round(firstSemGpa, 2))
    return firstSemGpa


def gpacalsem2():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 2....\n")

    while True:
        try:
            hs8251 = float(gradepoints(input("Enter Your Grade For Technical English (HS8251) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    hs8251 = hs8251 * 4

    while True:
        try:
            ma8251 = float(gradepoints(input("Enter Your Grade For Engineering Mathematics - 2(MA8251) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ma8251 = ma8251 * 4

    while True:
        try:
            ph8253 = float(gradepoints(input("Enter Your Grade For Physics For Electronics Engineering (PH8253) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ph8253 = ph8253 * 3

    while True:
        try:
            be8254 = float(gradepoints(input("Enter Your Grade For Basic Electrical and Instrumentation Engineering (BE8254) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    be8254 = be8254 * 3

    while True:
        try:
            ec8251 = float(gradepoints(input("Enter Your Grade For Circuit Analysis (EC8251) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8251 = ec8251 * 4

    while True:
        try:
            ec8252 = float(gradepoints(input("Enter Your Grade For Electronic Devices (EC8252) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8252 = ec8252 * 3

    while True:
        try:
            ec8261 = float(gradepoints(input("Enter Your Grade For Circuits and Devices Laboratory (GE8161) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8261 = ec8261 * 2

    while True:
        try:
            ge8261 = float(gradepoints(input("Enter Your Grade For Engineering Practices Lab (BS8151) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ge8261 = ge8261 * 2

    secSemGpa = float((hs8251 + ma8251 + ph8253 + be8254 + ec8251 + ec8252 + ec8261 + ge8261)) / 25
    print("\nYour Second Semester GPA is ", round(secSemGpa, 2))
    return secSemGpa


def gpacalsem3():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 3....\n")

    while True:
        try:
            ma8352 = float(gradepoints(input("Enter Your Grade For Linear Algebra and Partial Diff Equations (MA8352) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ma8352 = ma8352 * 4

    while True:
        try:
            ec8393 = float(gradepoints(input("Enter Your Grade For Fundamentals of Data Structures In C (EC8393) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8393 = ec8393 * 3

    while True:
        try:
            ec8351 = float(gradepoints(input("Enter Your Grade For Electronic Circuits-1 (EC8351) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8351 = ec8351 * 3

    while True:
        try:
            ec8352 = float(gradepoints(input("Enter Your Grade For Signals And Systems(EC8352) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8352 = ec8352 * 4

    while True:
        try:
            ec8392 = float(gradepoints(input("Enter Your Grade For Digital Electronics (EC8392) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8392 = ec8392 * 3

    while True:
        try:
            ec8391 = float(gradepoints(input("Enter Your Grade For Control Systems Engineering (EC8391) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8391 = ec8391 * 3

    while True:
        try:
            ec8381 = float(gradepoints(input("Enter Your Grade For FDS in C Laboratory (GE8161) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8381 = ec8381 * 2

    while True:
        try:
            ec8361 = float(gradepoints(input("Enter Your Grade For Analog and Digital Circuits Lab (BS8151) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8361 = ec8361 * 2

    while True:
        try:
            hs8381 = float(gradepoints(input("Enter Your Grade For Interpersonal Skills/Listening & Speaking (HS8381) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    hs8381 = hs8381 * 1

    thirdSemGpa = float((ma8352 + ec8393 + ec8351 + ec8352 + ec8392 + ec8391 + ec8381 + hs8381 + ec8361)) / 25
    print("\nYour Third Semester GPA is ", round(thirdSemGpa, 2))
    return thirdSemGpa


def gpacalsem4():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 4....\n")
    while True:
        try:
            ma8451 = float(gradepoints(input("Enter Your Grade For Probability and Random Processes (MA8451) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ma8451 = ma8451 * 4

    while True:
        try:
            ec8452 = float(gradepoints(input("Enter Your Grade For Electronic Circuits-2 (EC8452) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8452 = ec8452 * 3

    while True:
        try:
            ec8491 = float(gradepoints(input("Enter Your Grade For Communication Theory (EC8491) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8491 = ec8491 * 3

    while True:
        try:
            ec8451 = float(gradepoints(input("Enter Your Grade For Electromagnetic Fields (EC8451) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8451 = ec8451 * 4

    while True:
        try:
            ec8453 = float(gradepoints(input("Enter Your Grade For Linear Integrated Circuits (EC8453) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8453 = ec8453 * 3

    while True:
        try:
            ge8291 = float(gradepoints(input("Enter Your Grade For Environmental Science and Engineering (GE8291) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ge8291 = ge8291 * 3

    while True:
        try:
            ec8461 = float(gradepoints(input("Enter Your Grade For Circuits Design and Simulation Laboratory (EC8461) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8461 = ec8461 * 2

    while True:
        try:
            ec8462 = float(gradepoints(input("Enter Your Grade For Linear Integrated Circuits Laboratory (EC8462) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8462 = ec8462 * 2

    fourSemGpa = float((ma8451 + ec8452 + ec8491 + ec8451 + ec8453 + ge8291 + ec8461 + ec8462)) / 24
    print("\nYour Fourth Semester GPA is ", round(fourSemGpa, 2))
    return fourSemGpa


def gpacalsem5():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 5....\n")

    while True:
        try:
            ec8501 = float(gradepoints(input("Enter Your Grade For Digital Communication (EC8501) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8501 = ec8501 * 3


    while True:
        try:
            ec8553 = float(gradepoints(input("Enter Your Grade For Discrete-Time Signal Processing (EC8553) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8553 = ec8553 * 4

    while True:
        try:
            ec8552 = float(gradepoints(input("Enter Your Grade For Computer Architecture and Organization (EC8552 :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8552 = ec8552 * 3

    while True:
        try:
            ec8551 = float(gradepoints(input("Enter Your Grade For Communication Networks (EC8551) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8551 = ec8551 * 3

    while True:
        try:
            pe1 = float(gradepoints(input("Enter Your Grade For Professional Elective 1  :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    pe1 = pe1 * 3

    while True:
        try:
            oe1 = float(gradepoints(input("Enter Your Grade For Open Elective 1  :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    oe1 = oe1 * 3

    while True:
        try:
            ec8562 = float(gradepoints(input("Enter Your Grade For Digital Signal Processing Laboratory (EC8562) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8562 = ec8562 * 2

    while True:
        try:
            ec8561 = float(gradepoints(input("Enter Your Grade For Communications Networks Laboratory (EC8561) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8561 = ec8561 * 2

    while True:
        try:
            ec8563 = float(gradepoints(input("Enter Your Grade For Communications Networks Laboratory (EC8561) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8563 = ec8563 * 2

    fiveSemGpa = float((ec8501 + ec8553 + ec8552 + ec8551 + oe1 + pe1 + ec8562 + ec8563 + ec8561)) / 25
    print("\nYour Fifth Semester GPA is ", round(fiveSemGpa, 2))
    return fiveSemGpa


def gpacalsem6():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 6....\n")
    while True:
        try:
            ec8691 = float(gradepoints(input("Enter Your Grade For Microprocessors and Microcontrollers (EC8691) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8691 = ec8691 * 3

    while True:
        try:
            ec8095 = float(gradepoints(input("Enter Your Grade For VLSI Design (EC8095) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8095 = ec8095 * 3

    while True:
        try:
            ec8652 = float(gradepoints(input("Enter Your Grade For Wireless Communication (EC8652) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8652 = ec8652 * 3

    while True:
        try:
            mg8591 = float(gradepoints(input("Enter Your Grade For Principles of Management (MG8591) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    mg8591 = mg8591 * 3

    while True:
        try:
            ec8651 = float(gradepoints(input("Enter Your Grade For Transmission Lines and RF Systems (EC8651)  :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8651 = ec8651 * 3

    while True:
        try:
            pe2 = float(gradepoints(input("Enter Your Grade For Professional Elective 2  :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    pe2 = pe2 * 3

    while True:
        try:
            ec8681 = float(gradepoints(input("Enter Your Grade For Microprocessors and Microcontrollers Laboratory (EC8681) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8681 = ec8681 * 2

    while True:
        try:
            ec8661 = float(gradepoints(input("Enter Your Grade For VLSI Design Laboratory (EC8661) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8661 = ec8661 * 2

    while True:
        try:
            ec8611 = float(gradepoints(input("Enter Your Grade For Technical Seminar (EC8611) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8611 = ec8611 * 1

    sixSemGpa = float((ec8691 + ec8095 + ec8652 + mg8591 + ec8651 + pe2 + ec8681 + ec8661 + ec8611)) / 23
    print("\nYour Sixth Semester GPA is ", round(sixSemGpa, 2))
    return sixSemGpa


def gpacalsem7():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 7....\n")

    while True:
        try:
            ec8701 = float(gradepoints(input("Enter Your Grade For Antennas and Microwave (EC8701) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8701 = ec8701 * 3

    while True:
        try:
            ec8751 = float(gradepoints(input("Enter Your Grade For Optical Communication (EC8751) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8751 = ec8751 * 3

    while True:
        try:
            ec8791 = float(gradepoints(input("Enter Your Grade For Embedded and Real Time Systems (EC8791) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8791 = ec8791 * 3

    while True:
        try:
            ec8702 = float(gradepoints(input("Enter Your Grade For Ad hoc and Wireless Sensor Networks (EC8702) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8702 = ec8702 * 3

    while True:
        try:
            pe3 = float(gradepoints(input("Enter Your Grade For Professional Elective 2  :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    pe3 = pe3 * 3

    while True:
        try:
            oe2 = float(gradepoints(input("Enter Your Grade For Open Elective 2  :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    oe2 = oe2 * 3

    while True:
        try:
            ec8711 = float(gradepoints(input("Enter Your Grade For Embedded Laboratory (EC8711) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8711 = ec8711 * 2

    while True:
        try:
            ec8761 = float(gradepoints(input("Enter Your Grade For Advanced Communication Laboratory (EC8561) :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8761 = ec8761 * 2

    sevenSemGpa = float((ec8701 + ec8751 + ec8791 + ec8702 + pe3 + oe2 + ec8711 + ec8761)) / 22
    print("\nYour Seventh Semester GPA is ", round(sevenSemGpa, 2))
    return sevenSemGpa


def gpacalsem8():
    print("\nCALCULATING YOUR GPA FOR SEMESTER 8....\n")
    while True:
        try:
            pe4 = float(gradepoints(input("Enter Your Grade For Professional Elective 4  :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    pe4 = pe4 * 3

    while True:
        try:
            pe5 = float(gradepoints(input("Enter Your Grade For Professional Elective 5  :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    pe5 = pe5 * 3

    while True:
        try:
            ec8761 = float(gradepoints(input("Enter Your Grade For Project Work :")))
        except TypeError:
            print("Invalid Input Please Enter Appropriate Value !!!")
            continue
        else:
            break
    ec8761 = ec8761 * 10

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
        print("\nCALCULATING YOUR CGPA FOR ALL SEMESTERS ....\n")
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







