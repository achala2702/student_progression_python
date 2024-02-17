#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
#Any code taken form the other sources is referenced within my code solution.
#UoW Student ID: w1957443
#IIT Student ID: 20211280
#Date: 2022/11/22

#initializing variables
progression_list = ("Progress", "Progress(module trailer)", "Do not Progress-module retriever", "Excude")
histo_list = [0, 0, 0, 0]
result = 0
histo_outputs = ("Progress 1 :", "Trailer 1  :", "Retriever  :", "Excluded 1 :")
all_credit_list = []
all_progression_list = []
string_credits = ""
file1 = open("new.txt", "w")

#functions
def get_credits():

    """"getting credits, check the range and append it to a list
    """

    creditList = []
    nameList = ("PASS", "DEFER", "FAIL")
    num = 0

    while num < len(nameList):
        try:
            credit = int(input(f"Enter your total {nameList[num]} credits : "))
            if credit % 20 != 0:
                print("Out of range")

            else:
                creditList.append(credit)
                num += 1

        except ValueError:
            print("Integer requried")
            continue

    return creditList
    
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

def progression(creditList, progressList, proList, allCredits):

    """getting credtits and check the progression
    """
    
    outcome = ""
    strCreditList = []
    
    if creditList[0] == 120:
        outcome = progressList[0]

    elif creditList[0] == 100:
        outcome = progressList[1]

    elif (creditList[0] <= 80 and creditList[2] < 80):
        outcome = progressList[2]

    else:
        outcome = progressList[3]
    
    print('\n'+outcome)

    for val in creditList:
        strVal = str(val)
        strCreditList.append(strVal)
        
    proList.append(outcome)
    allCredits.append(strCreditList)
    
    return proList, allCredits

def histogram(creditList, histoList):

    """getting the marks of every attempt and mark the histrogram
    """

    if creditList[0] == 120:
        histoList[0] += 1
        
    elif creditList[0] == 100:
        histoList[1] += 1

    elif creditList[0] <= 80 and creditList[2] < 80:
        histoList[2] += 1

    else:
        histoList[3] += 1
    
    return histoList

#main program      
while True:
    print("Press 1 if you are a Student\nPress 2 if You are a Staff member")
    choice = input("\nEnter your choice : ")
    if choice == "1" or choice == "2":
        break
    else:
        print("\nInvalid Choice...\nTry Again!\n")
        continue

if choice == "1":
    
    credit_list = get_credits()
    
#check the whether the total credits == 120 or not
    check_valid = total_credits(credit_list)

#getting the progression if total credits == 120 
    if check_valid == True:
        st_progression = progression(credit_list, progression_list, all_progression_list, all_credit_list)
else:
    
    while True:
        credit_list = get_credits()
    
#check the whether the total credits == 120 or not
        check_valid = total_credits(credit_list)

#getting the progression if total credits == 120 
        if check_valid == True:
            st_progression, st_all_credits = progression(credit_list, progression_list, all_progression_list, all_credit_list)
            hist = histogram(credit_list, histo_list)

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
#printing the histogram
        else:
            print("\n" + "-" * 50)
            print("Histogram")
            for i in range(len(histo_outputs)):
                print(histo_outputs[i], '*' * hist[i])
                
            result = hist[0] + hist[1] + hist[2] + hist[3]
            print("\n", result, "outcomes in total.")
            print("-" * 50)
#printing part2
            print("\nPart 2:\n")
            for i in range(len(st_progression)):
                print(st_progression[i], '-', ', '.join(st_all_credits[i]))

#part 3
                line = f"\n{st_progression[i]} - {', '.join(st_all_credits[i])}"
                file1.write(line)
            file1.close()

            print("\nPart 3:")
        
            file2 = open("new.txt", "r")
            lines = file2.read()
            print(lines)
            file2.close() 
            break
