#I solved the Find the highest score challenge on @codeeval. #programming #hiring http://www.codeeval.com/browse/208
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        inputList = test.strip().split(" | ");
        firstList = inputList[0].strip().split(" ");
        dictionaryVals = {};
        for i in range (0,len(firstList)):
            dictionaryVals[i] = int(firstList[i].strip());
            
        for y in range(1,len(inputList)):
            nextList = inputList[y].strip().split(" ");
            for x in range (0,len(nextList)):
                if int(nextList[x].strip()) > dictionaryVals[x]:
                    dictionaryVals[x] = int(nextList[x].strip());
                    
                    
        stringOut = "";
        
        
        for key in dictionaryVals.keys():
            stringOut += str(dictionaryVals[key]) + " ";
        print stringOut.strip();
