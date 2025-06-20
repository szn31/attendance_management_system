import os 
from datetime import date

def take_attendance():
    with open("student.txt","r") as file:
        student_data = file.readlines()
        student_attendance = []
        for student in student_data:
            student = student.strip()
            print(student.split(","))
            print(student)
            roll = student.split(",")[0]
            name = student.split(",")[1]
            while True:
                print(roll, name)
                attendance = input("present (y/n)")
                if attendance == "y" or attendance == "n":
                    student_attendance.append(f"{roll},{name},{attendance}\n")
                    break
                else:
                    print("Invalid Input")
        with open(f"attendance/{date.today()}.txt","w") as file:
            file.writelines(student_attendance)

def view_attendance():
    date_input = input("Enter Date (yyyy-mm-dd) to View Attendance")
    if os.path.exists(f"attendance/{date_input}.txt"):
        with open(f"attendance/{date_input}.txt","r") as file:
            attendance_date = file.readlines()
            for attendance in attendance_date:
                print(attendance.strip())
    else:
        print("File Does not Exist")
            
    print("You Are on Take attendance function")
