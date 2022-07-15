from tabulate import tabulate
students            = [];
totalMarks          = 1200;
def getEnlgishMarks(n):
    try:
        englishMarks = int(input('Enter English Marks of '+n+': '))
    except ValueError as e:
        return getEnlgishMarks(n);

    if englishMarks <= 0 or englishMarks >= 150:
        print('Not a Valid Marks');
        return getEnlgishMarks(n);
    return englishMarks;
def getUrduMarks(n):
    try:
        urduMarks = int(input('Enter Urdu Marks of '+n+': '))
    except ValueError as e:
        return getUrduMarks(n);
    if urduMarks <= 0 or urduMarks >= 150:
        print('Not a Valid Marks');
        return getUrduMarks(n);
    return urduMarks;
def getMathMarks(n):
    try:
        mathMarks = int(input('Enter Math Marks of '+n+': '))
    except ValueError as e:
        return getMathMarks(n);
    
    if mathMarks <= 0 or mathMarks >= 150:
        print('Not a Valid Marks');
        return getMathMarks(n);
    return mathMarks;
    
def getIslamiatMarks(n):
    try:
        islamiatMarks = int(input('Enter Islamiat Marks of '+n+': '))
    except ValueError as e:
        return getIslamiatMarks(n);
    
    if islamiatMarks <= 0 or islamiatMarks >= 150:
        print('Not a Valid Marks');
        return getIslamiatMarks(n);
    return islamiatMarks;
def getPakStudiesMarks(n):
    try:
        psMarks = int(input('Enter Pak Studies Marks of '+n+': '))
    except ValueError as e:
        return getPakStudiesMarks(n);
    
    if psMarks <= 0 or psMarks >= 150:
        print('Not a Valid Marks');
        return getPakStudiesMarks(n);
    return psMarks;
def getScienceMarks(n):
    try:
        scienceMarks = int(input('Enter Science Marks of '+n+': '))
    except ValueError as e:
        return getScienceMarks(n);
    
    if scienceMarks <= 0 or scienceMarks >= 150:
        print('Not a Valid Marks');
        return getScienceMarks(n);
    return scienceMarks;
def getComputerMarks(n): 
    try:
        computerMarks = int(input('Enter Computer Marks of '+n+': '))
    except ValueError as e:
        return getComputerMarks(n);
    
    if computerMarks <= 0 or computerMarks >= 150:
        print('Not a Valid Marks');
        return getComputerMarks(n);
    return computerMarks;
def getChemistryMarks(n): 
    try:
        chemistryMarks = int(input('Enter Chemistry Marks of '+n+': '))
    except ValueError as e:
        return getChemistryMarks(n);
    
    if chemistryMarks <= 0 or chemistryMarks >= 150:
        print('Not a Valid Marks');
        return getChemistryMarks(n);
    return chemistryMarks;
def getNameOfStudent(): 
    # take the name of the student
    name            = input('Enter The Name Of Student: ');
    # validate if wrong input take
    if not name.isalpha():
        return getNameOfStudent();
    return name;
# add more record if want
def addMoreRecord():
    i = 0
    while i < 2:
        answer = input("Add more? (yes or no)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            return main();
            break
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            print("No")
            break
        else:
            i += 1
            if i < 2:
                print('Please enter yes or no')
                return addMoreRecord();

def gatherStudentData():
    # take the name of the student
    name            = getNameOfStudent();
    # taking subject marks for the student
    englishMarks    = getEnlgishMarks(name);
    urduMarks       = getUrduMarks(name);
    mathMarks       = getMathMarks(name);
    scienceMarks    = getScienceMarks(name);
    islamiatMarks   = getIslamiatMarks(name);
    psMarks         = getPakStudiesMarks(name);
    computerMarks   = getComputerMarks(name);
    chemistryMarks  = getChemistryMarks(name);
    
    person          = {
        "name":name,
        "english":englishMarks,
        "urdu":urduMarks,
        "math":mathMarks,
        "islamiat":islamiatMarks,
        "ps":psMarks,
        "science":scienceMarks,
        "computer":computerMarks,
        "chemistry":chemistryMarks,
    };
    
    return person;

# Calculate grade of each student
def assignGradeLetter(score):
    if score >= 70: return "A+"
    elif score >= 60: return "A"
    elif score >= 45: return "B"
    elif score >= 30: return "C"
    else : return "F"
# Calculate percentage of marks
def getMarksPercentage(marksList):
    return (sum(marksList[0:]) / totalMarks) * 100

def main():
    students.append(gatherStudentData());
    addMoreRecord();
# run main data gathering
main();

# format data as per table
tableData = [];
for student in students:
    data = [];
    data.append(student['name']);
    data.append(student['english']);
    data.append(student['urdu']);
    data.append(student['math']);
    data.append(student['islamiat']);
    data.append(student['ps']);
    data.append(student['science']);
    data.append(student['computer']);
    data.append(student['chemistry']);
    data.append(assignGradeLetter(getMarksPercentage(data[1:])));
    data.append(sum(data[1:9]));
    data.append(totalMarks);
    tableData.append(data);

# print table of the students
print(tabulate(tableData, headers=['name', 'English', 'Urdu', 'Match', 'Islamiat', 'Pak Studies', 'Science', 'Computer', 'Chmistry', 'Grade', 'Ob Marks', 'Total']));