marks = input()   
attendence = input()
project_completion_status = input()
if marks >= 60 and attendence >= 75:
    if project_completion_status == "yes":
        print("Eligible")
    print("Not Eligible")
    