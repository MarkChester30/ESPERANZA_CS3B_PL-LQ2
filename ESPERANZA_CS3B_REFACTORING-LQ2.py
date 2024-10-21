"""
Student Name: Mark Chester D. Esperanza
Course, Year, and Section: BSCS 3B
Quiz No.: Q2
"""

studentInfo = {
    "studentName": "Lewis Fonse",
    "studentAddress": "City of Candon, Ilocos Sur",
    "studentFavNum1": 25,   #Decalre the value as 25 as an Integer
    "studentAge": 25,   #Declare the value as 25 as an Integer
    "studentAllowance": float(500)     #Declare the value as 500 as an float with typecasting
}

classmateInfo = {
    "classmateName" : "Andrea Andres",
    "classmateAddress" : "City of Vigan, Ilocos Sur",
    "classmateFavNum1" :"18",     #Declare the value as 18 as an string
    "classmateAge" : "21",   #Declare the value 21 as an string
    "classmateAllowance" : "700"    #Declare the vallue as 700 as an string
}


namelength = [len(studentInfo["studentName"]), len(classmateInfo["classmateName"])]     #get the length of the studentNmae and classmateName

def AddressAndNames():
    if "Ilocos Sur" in studentInfo["studentAddress"] and "Ilocos Sur" in classmateInfo["classmateAddress"]:   #use as a condition if "Ilocos Sur" is in studentAdress AND cllassmateAddress
        print(studentInfo["studentName"], "is from", studentInfo["studentAddress"])    #output: Lewis Fonsi is from City of Candon, Ilocos Sur
        print(classmateInfo["classmateName"], "is from", classmateInfo["classmateAddress"])    #output: Andrea Andres is from City of Vigan, Ilocos Sur

        if namelength[0] > namelength[1]:
            print(f"{classmateInfo['classmateName']} has a longer name than {studentInfo['studentName']} with {namelength[1]} letters over {namelength[0]}")      #output: Andrea Andres has a longer name than Lewis Fonsi with 13 letters over 11 letters
        else:
            print(f"{studentInfo['studentName']} has a longer name than {classmateInfo['classmateName']} with {namelength[0]} letters over {namelength[1]}")       #output: Lewis Fonsi has a longer name than Andrea Andres with 11 letters over 12 letters
        
    elif "Ilocos Sur" in studentInfo['studentAddress'] and "Ilocos Sur" in classmateInfo['classmateAddress']:   #use as a condition elif "Ilocos Sur" is in studentAdress AND cllassmateAddress
        sName_Split = studentInfo["studentName"].split(" ")      #split the studentName with " " - a space as identifier of the splitter
        cName_Split = classmateInfo["classmateName"].split(" ")    #split the studentName with " " - a space as identifier of the splitter
        print(f"One among {sName_Split[0]} or {cName_Split[0]} lives in Ilocos Sur")    #output "One among Lewis or Andres lives in Ilocos Sur" use the sName_Split and cName_Split and use indexing
    else:
        print("None of the Students live in Ilocos Sur")

AddressAndNames()

classmateConvertAge = int(classmateInfo["classmateAge"])     #convert the age of classmate to an integer
print(f"The added age of {studentInfo['studentName']} and {classmateInfo['classmateName']} is {studentInfo['studentAge'] + classmateConvertAge}")      #output: The added age of Lewis Fonse and Andrea Andres is 46

classmateConvertFavNum = int(classmateInfo["classmateFavNum1"])    #convert the favenum of classmate to an integer
print(f"The subtracted value of favenum of {studentInfo['studentName']} and {classmateInfo['classmateName']} is {studentInfo['studentFavNum1'] - classmateConvertFavNum}")    #output: The subtracted value of favenum of Lewis Fonse and Andrea Andres is 7

classmateConvertAllowance = float(classmateInfo["classmateAllowance"])   #convert the allowance of classmate to an integer
combinedWeeklyAllowance = studentInfo["studentAllowance"] + classmateConvertAllowance     #add both allowances of the student and classmate
print(f"The weekly allowance of {studentInfo['studentName']} and {classmateInfo['classmateName']} is {combinedWeeklyAllowance:.2f}")     #output: The weekly allowance of Lewis Fonse and Andrea Andres is 1200.00

classList = [studentInfo["studentName"], classmateInfo["classmateName"]]      #declare the list of student and classmate name
classList_Ext = [studentInfo["studentAddress"], classmateInfo["classmateAddress"]]    #declare the list of student and classmate address

classList.extend(classList_Ext)   #extend the value of the classList with the classlist_Ext

for classlist in classList:
    print(classlist)   #print out the value of the classList using the for loop

classnumbers = [studentInfo["studentFavNum1"], studentInfo["studentAge"], studentInfo["studentAllowance"]]     #declare a list of all numerical vars of the student
classnumbers.append(classmateInfo["classmateAge"])     #append the classmateAge
classnumbers.append(classmateInfo["classmateFavNum1"])     #append the classmateFvaNum1
classnumbers.append(classmateConvertAllowance)     #append the classmateAllowance that was converted in to decimal

classnumbers = [str(item) for item in classnumbers]   #convert all the items to string

classnumbers.sort(reverse=True)   #sort the classNumbers

for classNum in classnumbers:
    print(classNum)   #print out the value of the classNumbers using the for loop

def quizTwo(studentNameCS):   #function which recieves a parameter studentNameCS
    print(f"Congratulations on Quiz 2 {studentNameCS}")   #output: Congratulations on Quez 2 Lewis Fonse

userName = input("Enter your Username: ")
quizTwo(userName)      #call the function quizTwo() passing a variable value of the name of the student of CS3B

print("Student of CS3B")      #output: Student of CS3B