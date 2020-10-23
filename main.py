percentData = []
subjectCodeDist = {}
subjectPI = {}
totalPI = []
school_info = []

def calSubjectCodeGrade(studentDetails , subDetails):
    global subjectCodeDist
    i=2
    j=1
    while(i<len(studentDetails)):
        ##print(i)
        if studentDetails[i].isdigit():
            break
        i+=1
    ##print("here")
    while(i<len(studentDetails) and studentDetails[i].isdigit()):
        ##print(i)
        subjectCode = studentDetails[i]
        subjectGrade = subDetails[j]
        if not(subjectCode in subjectCodeDist):
            tempList = {'A1': 0,'A2': 0,'B1': 0,'B2': 0,'C1': 0,'C2': 0,'D1': 0,'D2': 0,'E': 0}
            tempList[subjectGrade]=tempList[subjectGrade]+1
            subjectCodeDist[subjectCode] = tempList
        else:
            tempList = subjectCodeDist[subjectCode]
            tempList[subjectGrade]=tempList[subjectGrade]+1
            subjectCodeDist[subjectCode] = tempList
        i+=1
        j+=2

def calPercent(studentDetails , subDetails):
    global percentData
    rollNo = studentDetails[0]
    totalMarks = 0
    i = 2
    tempName = studentDetails[i]
    while(not(studentDetails[i+1].isdigit())):
        tempName = tempName+" "+studentDetails[i+1]
        i+=1
    name = tempName
    for mark in subDetails:
        if mark.isdigit():
            totalMarks = totalMarks+ int(mark)
    percentage = '{0:.2f}'.format(100*totalMarks / 500)
    ##print(rollNo, name, percentage)
    ##print("%.3f"%percentage)
    tempList = {'rollNo': rollNo,'name': name,'percentage': percentage}
    ##print("tempList ")
    ##print(tempList)
    percentData.append(tempList)
    ##print("percentData ")
    ##print(percentData)

def readFile(path) :
    global school_info
    file = open(path,'r')
    rawlines = file.readlines()
    ##print(rawlines)
    lines = []
    j = 0
    while (j<len(rawlines)):
        listRawLines = rawlines[j].split(' ')
        if listRawLines[0].isdigit():
            lines.append(rawlines[j])
            lines.append(rawlines[j+1])
            j = j+2
            continue
        j= j+1

    #print(lines)
    length = len(lines)
    i = 0

    while(i < length):
       linedetails = lines[i].split(' ')
       preprocess = []
       for l in linedetails:
           if l != '':
               preprocess.append(l)
       if preprocess[0].isdigit():
           break
       i = i+1

    while(i<length-1):
       linedetails = lines[i].split(' ')
       prelinedetails = []
       finallinedetails = []
       for l in linedetails:
           if l != '':
               prelinedetails.append(l)
       if prelinedetails[0].isdigit():
           finallinedetails = prelinedetails.copy()
       markslinedetails = lines[i+1].split(' ')
       premarkslinedetails = []
       finalmarkslinedetails = []
       for l in markslinedetails:
           if l != '':
               premarkslinedetails.append(l)
       if premarkslinedetails[0].isdigit():
           finalmarkslinedetails = premarkslinedetails.copy()
       if finallinedetails and finalmarkslinedetails:
        '''
        #print("sending following details: \n")
        #print(finallinedetails)
        #print(finalmarkslinedetails)
        #print("\n")
        '''
        calPercent(finallinedetails , finalmarkslinedetails)
        calSubjectCodeGrade(finallinedetails,finalmarkslinedetails)
        piCalculator()
       #studentDetailsDict = {'roll' : }
       i = i + 2

def myFunc(e):
  return e['percentage']

def saveToFile(name):
    file = open(name,'w')
    for line in percentData:
        file.write(line['rollNo']+"     "+line['name']+"        "+str(line['percentage'])+"   \n")
    file.close()

def saveToFile_sub(name,subjectPI,totalPI):
    file = open(name, 'w')
    for key,value in subjectCodeDist.items():
        file.write(str(key)+"     A1 = "+str(value['A1'])+"     A2 = "+str(value['A2'])+"     B1 = "+str(value['B1'])+"     B2 = "+str(value['B2'])+"     C1 = "+str(value['C1'])+"     C2 = "+str(value['C2'])+"     D1 = "+str(value['D1'])+"     D2 = "+str(value['D2'])+"     E = "+str(value['E'])+"     PI = "+ str(subjectPI[key])+"\n")
    file.write("\nClass PI = "+str(totalPI))

    file.close()

def piCalculator():
    #readFile()
    ##print(percentData)
    percentData.sort(key=myFunc,reverse=True)
    ##print(percentData)
    saveToFile('percentage.txt')
    ##print(subjectCodeDist)
    global subjectPI
    global totalPI
    totalA1 = 0
    totalA2 = 0
    totalB1 = 0
    totalB2 = 0
    totalC1 = 0
    totalC2 = 0
    totalD1 = 0
    totalD2 = 0
    totalE = 0
    for key,value in subjectCodeDist.items():
        totalA1 = totalA1+value['A1']
        totalA2 = totalA2 + value['A2']
        totalB1 = totalB1 + value['B1']
        totalB2 = totalB2 + value['B2']
        totalC1 = totalC1 + value['C1']
        totalC2 = totalC2 + value['C2']
        totalD1 = totalD1 + value['D1']
        totalD2 = totalD2 + value['D2']
        totalE = totalE + value['E']
        numberOfStudents = value['A1']+value['A2']+value['B1']+value['B2']+value['C1']+value['C2']+value['D1']+value['D2']+value['E']
        x = 8 * value['A1'] + 7 * value['A2'] + 6 * value['B1'] + 5 * value['B2'] + 4 * value['C1'] + 3 * value['C2'] + 2 *value['D1'] + 1 * value['D2']
        subjectPI[key] = (x * 100) / (numberOfStudents * 8)
    #numberOfStudent = totalA1+totalA2+totalB1+totalB2+totalC1+totalC2+totalD1+totalD2+totalE
    numberOfStudent = len(percentData)
    x = 8 * totalA1 + 7 * totalA2 + 6 * totalB1 + 5 * totalB2 + 4 * totalC1 + 3 * totalC2 + 2 *totalD1 + 1 * totalD2
    totalPI.append((x * 100) / (numberOfStudent * 40))
    saveToFile_sub('SubjectCodeGrade.txt',subjectPI,totalPI)