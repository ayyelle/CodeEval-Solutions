#I solved the Fizz Buzz challenge on @codeeval. #programming #hiring http://www.codeeval.com/browse/1
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        inputValue = test.strip();
        splitInputValue = inputValue.split(" ");
        intValueOne = int(splitInputValue[0]);
        intValueTwo = int(splitInputValue[1]);
        intValueThree = int(splitInputValue[2]);
        stringOutput="";
        for i in range(1,intValueThree+1):
            if (i%intValueTwo == 0) and (i%intValueOne ==0):
                stringOutput += " FB"
            elif(i%intValueOne ==0):
                stringOutput +=" F"
            elif(i%intValueTwo == 0):
                stringOutput +=" B"
            else:
                stringOutput +=" "+ str(i);
        print stringOutput.strip();
