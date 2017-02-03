#I solved the Stepwise word challenge on @codeeval. #programming #hiring http://www.codeeval.com/browse/202
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        inputList = test.strip().split(" ");
        maxIndex = 0;
        for i in range(0,len(inputList)):
            if (len(inputList[i]) > len(inputList[maxIndex])):
                maxIndex = i;
                
        longestWord = inputList[maxIndex]
        outputString = "";
        for y in range(0,len(longestWord)):
            for x in range (0,y):
                outputString+="*"
            outputString += longestWord[y] +" ";
            
        print outputString.strip()
