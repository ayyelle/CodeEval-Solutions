#I solved the Swap Elements challenge on @codeeval. #programming #hiring http://www.codeeval.com/browse/112
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        inputParts = test.strip().split(" : ")
        listTo = inputParts[0].strip().split(" ")
        valuesTo = inputParts[1].strip().split(",")
    
        for group in valuesTo:
            strippedGroup = group.strip();
            groupArray = strippedGroup.split("-")
            value1 = listTo[int(groupArray[0])]
            value2 = listTo[int(groupArray[1])]
            listTo[int(groupArray[0])] = value2
            listTo[int(groupArray[1])] = value1
    
        stringOutput  = ""
        for item in listTo:
            stringOutput += item + " ";
        
        print (stringOutput.strip());
