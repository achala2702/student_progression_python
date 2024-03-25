#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
#Any code taken form the other sources is referenced within my code solution.
#UoW Student ID: w1957443
#IIT Student ID: 20211280
#Date: 2022/11/22

#initializing variables
name_list = ["PASS", "DEFER", "FAIL"]
progression_list = ["Progress", "Progress(module trailer)", "Do not Progress-module retriever", "Excude"]
string_credits = ""
student_id = ""
stNo = 0
progress_credits = []
student_ids = []
progress_dict = {}

#functions
def total_credits(credit_list):

    """getting credt list and check whether the total credits == 120
    """
    
    total = 0
    outcome = ""

    for credit in credit_list:
        total += credit       
    if total != 120:
        print("Total incorrect")
        outcome = False
    else:
        outcome = True

    return outcome

def progression(creditList, progressList, progressCredits):

    """creating a list contains progressions + credits to make a dictionery
    """
    
    outcome = ""
    strCreditList = []
    line = ""

    if creditList[0] == 120:
        line = str(progressList[0]) + " - " + str(creditList)

    elif creditList[0] == 100:
        line = str(progressList[1]) + " - " + str(creditList)
        
    elif (creditList[0] <= 80 and creditList[2] < 80):
        line = str(progressList[2]) + " - " + str(creditList)

    else:
        line = str(progressList[3]) + " - " + str(creditList)

    progressCredits.append(line)
    
    return progressCredits

#main program
while True:
#getting the student id
    while True:
        student_id = input("\nEnter the Your Student ID : ")
        st_id = student_id.lower()

        if len(st_id) == 8 and st_id[0] == 'w' and st_id not in student_ids and st_id[1:].isdigit():
            stNo = int(st_id[1:])
            break

        else:
            print("Check the Student ID! \n(May be its invalid or used before)")
            continue

#initializing variables
    credit_list = []
    num = 0

#getting the credits from user
    while num < len(name_list):
        try:
            credit = int(input(f"Enter your total {name_list[num]} credits : "))
            if credit % 20 != 0:
                print("Out of range")
            else:
                credit_list.append(credit)
                num += 1

        except ValueError:
            print("Integer requried")
            continue
#check the whether the total credits == 120 or not
    check_valid = total_credits(credit_list)

#appending student id to list and creating a list of progressions + credits if total_credits == 120
    if check_valid == True:
        student_ids.append(st_id)
        st_progression_credits = progression(credit_list, progression_list, progress_credits)

#check wether user want to continue or not
    while True:
        to_continue = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results : ")

        if to_continue == 'y' or to_continue == 'Y' or to_continue == 'q' or to_continue == 'Q':
            conti = to_continue.lower()
            break    
        else:
            print("\nInvalid choice")
            continue
    if conti == 'y':
        continue
    else:
#printing the dictionery
        print("\nPart 4 :\n")
        for i in range(len(student_ids)):
            progress_dict[student_ids[i]] = st_progression_credits[i]

        for key, val in progress_dict.items():
            print(f"{key} : {val}")
        break
