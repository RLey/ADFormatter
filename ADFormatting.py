# script to format usernames to be added to AD

def readInFile(filename):
    inputs = open(filename, "r")
    array = []
    for line in inputs:
        array.append(line.strip("\n"))
    return array

def outputNewFile(inputData):
    file = open("results", "w")
    for line in inputData:
        file.write(line + ";")
    file.close()
    
filename1 = input("What is the file you want to reformat?\n")
dataArray = readInFile(filename1)
outputNewFile(dataArray)